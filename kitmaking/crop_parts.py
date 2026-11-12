"""Find every box in a parts picture and crop the part inside it (tight, with a margin), one PNG per part."""
import sys, cv2, numpy as np
from pathlib import Path
src = Path(sys.argv[1]); out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
im = cv2.imread(str(src)); h, w = im.shape[:2]
bg = np.median(im[5:40, 5:40].reshape(-1, 3), 0)
diff = np.abs(im.astype(int) - bg).sum(2)
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(int); sat = im.max(2).astype(int) - im.min(2).astype(int)
border = ((sat < 16) & (diff > 18) & (diff < 330)).astype(np.uint8)       # grey box lines, from faint to mid grey
k = max(3, w // 400)
lines = cv2.morphologyEx(border, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (w // 25, 1))) | \
        cv2.morphologyEx(border, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, h // 25)))
thick = cv2.morphologyEx(border, cv2.MORPH_OPEN, np.ones((5 * k, 5 * k), np.uint8))   # filled grey shapes (tyres), not lines
lines = lines & (1 - cv2.dilate(thick, np.ones((3, 3), np.uint8)))
lines = cv2.dilate(lines, np.ones((k, k), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats((1 - lines).astype(np.uint8), 4)
ink = (diff > 60) & (lines == 0)
cells = []
for i in range(1, n):
    x, y, bw, bh, a = st[i]
    if a < 0.004 * w * h or bw > 0.95 * w or bh > 0.95 * h: continue
    s = 3 * k; cx0, cy0, cx1, cy1 = x + s, y + s, x + bw - s, y + bh - s
    m = (lab[cy0:cy1, cx0:cx1] == i) & ink[cy0:cy1, cx0:cx1]
    ys, xs = np.where(m)
    if len(xs) < 200: continue
    pad = k * 4
    x0, y0 = max(cx0, cx0 + xs.min() - pad), max(cy0, cy0 + ys.min() - pad); x1, y1 = min(cx1, cx0 + xs.max() + pad), min(cy1, cy0 + ys.max() + pad)
    cells.append((y // (h // 20), x, (x0, y0, x1, y1)))
cells.sort()
for j, (_, _, (x0, y0, x1, y1)) in enumerate(cells, 1):
    crop = im[y0:y1, x0:x1].copy()
    cv2.imwrite(str(out / f'p{j:02d}.png'), crop)
print(src.stem, len(cells), 'parts')
