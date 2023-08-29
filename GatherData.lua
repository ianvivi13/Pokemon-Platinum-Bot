local file = io.open("game_data.txt", "w")
if file then
    file:write("HELLO WORLD")
    file:close()
else
    print("Error opening the file for writing.")
end