stickbug = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠏⢉⠙⣿⠉⢉⣹⡉⠉⣉⣿⣿⡟⢉⠙⢿⡉⠉⣉⡏⢹⡟⢉⠉⢻⡏⢹⠋⣽⣿⣿⠉⣉⠙⣟⠉⣿⠉⣿⠋⡉⠻⡿⠋⡉⢻⡏⠉⣉⣿⠉⣉⠙⣿⣿⣿⠉⣿⣿⠏⢉⠙⣿⠉⣿⣿⣿⣿
⣿⣿⠀⣿⣦⣿⠀⠿⢿⣿⠀⣿⣿⣿⣇⠘⢷⣾⣿⠀⣿⡇⢸⡇⢸⣧⣼⡇⠈⢀⣿⣿⣿⠀⠟⢀⣿⠀⣿⠀⣿⠀⣿⣴⡇⠀⣷⣴⡇⠘⠿⣿⠀⣿⠀⣿⣿⣿⠀⣿⣿⠀⣿⠀⣿⠀⣿⣿⣿⣿
⣿⣿⠀⣿⠀⣿⠀⣶⣾⣿⠀⣿⣿⣿⡟⢷⡀⢹⣿⠀⣿⡇⢸⡇⢸⡟⢻⡇⢠⠀⣿⣿⣿⠀⣶⠀⡟⠀⣿⠀⣿⠀⣧⠀⡇⠀⡇⠀⡇⢠⣶⣿⠀⣿⠀⣿⣿⣿⠀⣿⣿⠀⣿⠀⣿⠀⣿⣿⣿⣿
⣿⣿⣄⣉⣀⣿⣀⣉⣹⣿⣀⣿⣿⣿⣇⣈⣁⣼⣿⣀⣿⣇⣸⣇⣈⣁⣼⣇⣸⣄⣹⣿⣿⣀⣉⣀⣿⣀⣉⣠⣿⣀⣉⣀⣧⣀⣁⣀⣇⣈⣉⣿⣀⣉⣀⣿⣿⣿⣀⣙⣻⣄⣉⣀⣿⣀⣙⣻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣋⣥⣴⣾⢏⣼⣿⣷⣄⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣩⣤⣶⣿⣿⣿⣿⡏⣼⣿⣿⡿⢋⣤⣦⡀⠈⠙⠛⠛⠛⠟⠛⠛⠛⠛⢛⣙⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⡟⣸⣿⡿⢋⣴⣿⣿⣿⡇⠀⣶⣶⣶⣶⣶⣶⣶⣤⣤⡍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⠟⣡⣾⣿⣿⣿⡿⢠⡆⣽⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⣿⣸⣿⣿⣿⣿⣿⢡⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⡇⣿⣿⣿⣿⣿⡟⠼⣣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣶⣶⣶⣶⣤⣤⣤⣀⣈⣉⣉⡉⠉⠛⠛⠛⠰⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡟⣾⣿⣿⢹⣿⣿⣿⣿⣿⡇⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣦⣤⣤⣄⣈⣉⣉⣁⣉⠉⠋⠘⠻⠿⠿⠿⠿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣬⣍⣉⣉⣉⡛⠛⠛⠛⠿⠿⠿⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣄⣉⣉⣉⣉⠛⠛⠛⠿⠿⠿⠿⠿
"""