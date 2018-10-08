_input = input("Enter input: ")
_output = []

if '(' not in _input:
    count = int((len(_input) / 2) // 1)

    for x in range(0, len(_input)):
        if x is 0:
            _output.append(f"E {_input[1]} E")
            _input = _input.replace(_input[0:2], '')
        elif x < count:
            _output.append(f"{_output[x - 1].replace('E', 'num', 1)}  {_input[1]} E")
            _input = _input.replace(_input[0:2], '')
        else:
            _output.append(_output[x - 1].replace('E', 'num', 1))
            _input = _input.replace(_input[0:2], '')

    for x in range(0, len(_output)):
        if _output[x] is not _output[x - 1]:
            print(f"E => {_output[x]}")
elif _input[0] is '(' and _input[-1] is ')':
    newInput = _input.replace('(', '').replace(')', '')

    count = int((len(newInput) / 2) // 1)

    for x in range(0, len(newInput)):
        if x is 0:
            _output.append(f"E {newInput[1]} E")
            newInput = newInput.replace(newInput[0:2], '')
        elif x < count:
            _output.append(f"{_output[x - 1].replace('E', 'num', 1)}  {newInput[1]} E")
            newInput = newInput.replace(newInput[0:2], '')
        else:
            _output.append(_output[x - 1].replace('E', 'num', 1))
            newInput = newInput.replace(newInput[0:2], '')

    print("E => (E)")
    for x in range(0, len(_output)):
        if _output[x] is not _output[x - 1]:
            print(f"E => ({_output[x]})")
else:
    print("Thank you for the wonderful Input!")
