import raylib as rl

# Initialize window
rl.InitWindow(800, 450, "My First Raylib Game")

# Set target FPS
rl.SetTargetFPS(60)

# Main game loop
while not rl.WindowShouldClose():
    # Update
    
    # Draw
    rl.BeginDrawing()
    rl.ClearBackground(rl.RAYWHITE)
    rl.DrawText("Hello, Raylib!", 190, 200, 20, rl.DARKGRAY)
    rl.EndDrawing()

# Cleanup
rl.CloseWindow()
