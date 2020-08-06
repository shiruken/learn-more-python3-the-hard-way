import sys

args = iter(sys.argv[1:])
positional = []
for arg in args:

    if arg in ("-c", "--copy"):
        print("Copy mode enabled")
        continue

    if arg in ("-d", "--delete"):
        print("Delete mode enabled")
        continue

    if arg in ("-a", "--archive"):
        print("Archive mode enabled")
        continue

    if arg in ("-p", "--path"):
        path = next(args, None)
        print(f"Path set to {path}")
        continue

    if arg in ("-t", "--timeout"):
        time = next(args, None)
        print(f"Timeout set to {time} seconds")
        continue

    if arg in ("-s", "--start"):
        start = next(args, None)
        print(f"Start set to {start}")
        continue

    if arg in ("-h", "--help"):
        print("Help:")
        print("  --copy (-c): Enable copy mode")
        print("  --delete (-d): Enable delete mode")
        print("  --archive (-a): Enable archive mode")
        print("  --path (-p): Set path option")
        print("  --timeout (-t): Set timeout option in seconds")
        print("  --start (-s): Set start option")
        continue

    positional.append(arg)

if positional:
    print(f"Positional arguments: {positional}")
