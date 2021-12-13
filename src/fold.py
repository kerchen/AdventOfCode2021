

def parse_instructions(input_data: str) -> tuple:
    dots = []
    folds = []

    for line in input_data.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('fold along '):
            fold_data = line[11:].split('=')
            folds.append((fold_data[0], int(fold_data[1])))
        else:
            coord_str = line.split(',')
            dots.append((int(coord_str[0]), int(coord_str[1])))

    return dots, folds
