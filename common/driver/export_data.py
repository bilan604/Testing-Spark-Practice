

def export_as_txt(file_name):
    dd_export = as_dd(grs.JSON_data)
    with open(file_name, "w+") as f:
        f.write( ", ".join([str(k) for k in dd_export.keys()]) + '\n')
        export = list(dd_export.values())
        for r1, p, c, r2 in zip(export[0], export[1], export[2], export[3]):
            f.write(", ".join([str(item) for item in (r1,p,c,r2)]) + '\n')
        f.close()
    return None