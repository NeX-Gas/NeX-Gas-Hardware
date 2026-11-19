#!/usr/bin/env python3
"""Rotate the exported STL into the support-free print pose and write a new STL.

  tray : print z =  model y + 25   (back wall on the bed, opening up)
  lid  : print z = 25 - model y    (outer face on the bed, bosses up)

Both mappings are proper rotations (det = +1), not mirrors.
"""
import sys

TRAY_Y_MIN = -25.0
LID_Y_OUTER = 25.0


def transform(mode, v):
    x, y, z = v
    if mode == "tray":
        return (x, -z, y - TRAY_Y_MIN)
    if mode == "lid":
        return (x, z, LID_Y_OUTER - y)
    raise SystemExit("mode must be tray or lid")


def read_ascii_stl(path):
    verts = []
    with open(path, "r", errors="ignore") as f:
        for line in f:
            s = line.strip()
            if s.startswith("vertex "):
                _, a, b, c = s.split()
                verts.append((float(a), float(b), float(c)))
    if len(verts) % 3:
        raise SystemExit("vertex count is not a multiple of 3")
    return [verts[i:i + 3] for i in range(0, len(verts), 3)]


def normal(tri):
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = tri
    ux, uy, uz = bx - ax, by - ay, bz - az
    vx, vy, vz = cx - ax, cy - ay, cz - az
    nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
    n = (nx * nx + ny * ny + nz * nz) ** 0.5 or 1.0
    return nx / n, ny / n, nz / n


def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: orient_for_print.py <in.stl> <out.stl> tray|lid")
    src, dst, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    tris = [[transform(mode, v) for v in tri] for tri in read_ascii_stl(src)]

    with open(dst, "w") as f:
        f.write("solid print\n")
        for tri in tris:
            n = normal(tri)
            f.write("  facet normal %.6e %.6e %.6e\n    outer loop\n" % n)
            for v in tri:
                f.write("      vertex %.6f %.6f %.6f\n" % v)
            f.write("    endloop\n  endfacet\n")
        f.write("endsolid print\n")

    xs = [v[0] for tri in tris for v in tri]
    ys = [v[1] for tri in tris for v in tri]
    zs = [v[2] for tri in tris for v in tri]
    print("%s: %d facets, bbox X %.2f..%.2f  Y %.2f..%.2f  Z %.2f..%.2f" %
          (dst, len(tris), min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)))


if __name__ == "__main__":
    main()
