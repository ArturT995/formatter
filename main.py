path = "input.txt"

def get_input(path):
    with open(path) as f:
        text = f.read(30000)
        return text
    
    
def format_text(text):
    lines = text.split("\n")
    unbracketed_lines = []
    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            continue
        unbracketed_lines.append(line)

    def has_timestamp(line):
        return '—' in line and ('PM' in line or 'AM' in line) and ":" in line
    
    formatted_lines = []
    i = 0
    while i < len(unbracketed_lines):
        current = unbracketed_lines[i]
        if i + 1 < len(unbracketed_lines):
            next = unbracketed_lines[i+1]
        if has_timestamp(current):
            formatted_lines.append(current)
            i += 1
        elif has_timestamp(next) and next.startswith(' —'):
            join_time = current + " " + next
            formatted_lines.append(join_time)
            i += 2
        else:
            formatted_lines.append(current)
            i += 1
    
    for i in range(0, len(formatted_lines)-1):
        line = formatted_lines[i]
        if has_timestamp(line):
            formatted_lines[i] = "\n" + line
    
    result = "\n".join(formatted_lines)
    return result


def write_text(result):
    with open("output.txt", "w") as f:
        f.write(result.strip())

def main():
    text = get_input(path)
    result = format_text(text)
    write_text(result)
    return result.strip()

main()

if __name__ == "__main__":
    main()
