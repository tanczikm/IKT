def euro_valto(forint):
    euro = forint / 400
    return euro

penzem = euro_valto(8000)

if penzem < 50:
    print(f"Ez még kevés, csak {penzem} euród van.")