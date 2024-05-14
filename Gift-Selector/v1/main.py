# imports
import pygame
import random

# Constants
GIFT_LIST = 'gifts.txt'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCROLLBAR_COLOR = (150, 150, 150)
SCROLLBAR_BUTTON_COLOR = (100, 100, 100)
ITEM_HEIGHT = 30  # Height of each item in the menu
SCROLL_SPEED = 20  # Speed of scrolling

def unique_list(options):
    return set(options)

def shuffle_contents(options):
    return random.shuffle(options)

def list_to_string(selected_list):
    # Convert a list to a string
    if selected_list == None:
        print("No valid list found.")
    try:
        string = ' '.join(str(list_prime) for list_prime in selected_list)
        return string
    except ValueError:
        print("Invalid input! Please enter a valid list.")

def read_notepad(notepad): 
    # Reading contents of the notepad and shuffling them
    try:
        with open(notepad, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print("Number of lines read from the file: ", len(lines))
            shuffle_contents(lines)
            unique_lines = unique_list(lines)
            print("Number of lines after shuffling: ", len(unique_lines))
            start_index, end_index = 0, len(unique_lines)
            return list(unique_lines)[start_index : end_index + 1]
    except FileNotFoundError:
        print("File not Found!")

def save_top_10(options):
    # Proceed with saving the top 10 options
    with open('top_10.txt', 'w') as file:
        file.write(''.join(options[:10]).title().strip())
    return "Top 10 have been saved."

def display_on_gui(options):
    # Starting pygame
    pygame.init()

    # Define minimum and maximum window size
    MIN_WINDOW_SIZE = (300, 400)
    MAX_WINDOW_SIZE = (1050, 1000)
    
    # Window Parameters
    window_height = 550  # Increased height to accommodate the title
    window_width = 550
    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Gift Options Ranked at Random")

    # Display Font
    font = pygame.font.SysFont("Arial", 24)
    bold_font = pygame.font.SysFont("Arial", 24, bold=True)

    # Colors Display
    text_color = WHITE
    background_color = BLACK

    # Variables for Scrolling
    scroll_offset = 0
    is_scrolling = False
    scroll_start_pos = 0

    # Message Text
    message_text = ""
    message_font = pygame.font.SysFont("Arial", 20)
    # message_color = (255, 255, 0)
    message_alpha = 255  # Initial alpha value
    message_display_time = 0

    # Clock for managing FPS
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        window.fill(background_color)

        # Draw title
        title_surface = bold_font.render(f"{len(options) - 2} Gift Options Ranked at Random", True, text_color)
        title_height = title_surface.get_height()  # Get the height of the title surface
        window.blit(title_surface, ((window_width - title_surface.get_width()) // 2, 10 - scroll_offset))

        # Draw save top 50 button
        save_top_10_text = bold_font.render("Save Top 10", True, BLACK)
        save_top_10_rect = save_top_10_text.get_rect(bottomright=(window_width - 22, window_height - 90))
        save_top_10_color = (255, 255, 0)  # Default color
        if save_top_10_rect.collidepoint(pygame.mouse.get_pos()):
            save_top_10_color = (255, 255, 150)  # Change color on hover
        pygame.draw.rect(window, save_top_10_color, save_top_10_rect)
        window.blit(save_top_10_text, save_top_10_rect)

        # Draw refresh button
        refresh_button_text = bold_font.render("Refresh", True, BLACK)
        refresh_button_rect = refresh_button_text.get_rect(bottomright=(window_width - 22, window_height - 50))
        refresh_button_color = (0, 255, 0)  # Default color
        if refresh_button_rect.collidepoint(pygame.mouse.get_pos()):
            refresh_button_color = (150, 255, 150)  # Change color on hover
        pygame.draw.rect(window, refresh_button_color, refresh_button_rect)
        window.blit(refresh_button_text, refresh_button_rect)

        # Draw exit button
        exit_button_text = bold_font.render("Exit", True, WHITE)
        exit_button_rect = exit_button_text.get_rect(bottomright=(window_width - 22, window_height - 10))
        exit_button_color = (255, 0, 0)  # Default color
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            exit_button_color = (255, 150, 150)  # Change color on hover
        pygame.draw.rect(window, exit_button_color, exit_button_rect)
        window.blit(exit_button_text, exit_button_rect)

        # Draw message
        if message_text:
            message_surface = message_font.render(message_text, True, (255, 255, 0, message_alpha))
            window.blit(message_surface, ((window_width - message_surface.get_width()) - 22, window_height - (window_height - 50)))

            # Update message alpha and display time
            if pygame.time.get_ticks() - message_display_time > 3000:  # 3 seconds
                message_alpha -= 3  # Adjust this value to control fade speed
                if message_alpha <= 0:
                    message_text = ""  # Clear message when fully faded
                    message_alpha = 255  # Reset alpha for next message
            else:
                message_display_time = pygame.time.get_ticks()  # Update display time

        # Draw options
        height_adjustment = title_height + 20
        total_height = len(options) * ITEM_HEIGHT
        max_scroll = max(total_height - window_height, 0)
        y = height_adjustment - scroll_offset

        # Draw scrollbar
        if max_scroll > 0:
            scrollbar_height = (window_height * window_height) / (len(options) * ITEM_HEIGHT)
            scrollbar_offset = (scroll_offset * (window_height - scrollbar_height)) / max_scroll
            pygame.draw.rect(window, SCROLLBAR_COLOR, (window_width - 20, 0, 20, window_height))
            pygame.draw.rect(window, SCROLLBAR_BUTTON_COLOR, (window_width - 20, scrollbar_offset, 20, scrollbar_height))

        for idx, option in enumerate(options, start=1):
            option_text = option.strip()  # Convert entire string to title case
            words = option_text.split()
            for i, word in enumerate(words):
                if not word.isupper():
                    words[i] = word.title()  # Convert non-uppercase words to title case
            option_text = list_to_string(words)
            numbered_text = f"{idx}. {option_text}"
            bold_text_surface = font.render(numbered_text, True, text_color)

            # Check if the option is within the visible window range
            if y < window_height - ITEM_HEIGHT and (y + ITEM_HEIGHT) > 0:
                window.blit(bold_text_surface, (10, y))
            y += ITEM_HEIGHT

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    scroll_offset -= SCROLL_SPEED
                elif event.button == 5:  # Scroll down
                    scroll_offset += SCROLL_SPEED
                elif event.button == 1:  # Left mouse button
                    if save_top_10_rect.collidepoint(event.pos):
                        message_text = save_top_10(options)
                    elif refresh_button_rect.collidepoint(event.pos):
                        shuffle_contents(options)
                        message_text = "Contents of the list have been refreshed."
                    elif exit_button_rect.collidepoint(event.pos):
                        running = False
                    elif window_width - 20 <= event.pos[0] <= window_width:
                        if max_scroll > 0:
                            scrollbar_height = window_height * window_height / (len(options) * ITEM_HEIGHT)
                            scrollbar_offset = scroll_offset * (window_height - scrollbar_height) / max_scroll
                            if scrollbar_offset <= event.pos[1] <= scrollbar_offset + scrollbar_height:
                                is_scrolling = True
                                scroll_start_pos = event.pos[1] - scrollbar_offset
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    is_scrolling = False
            elif event.type == pygame.MOUSEMOTION:
                if is_scrolling:
                    new_scrollbar_offset = event.pos[1] - scroll_start_pos
                    if max_scroll > 0:
                        scrollbar_height = window_height * window_height / (len(options) * ITEM_HEIGHT)
                        scrollbar_offset = min(max(new_scrollbar_offset, 0), window_height - scrollbar_height)
                        scroll_offset = int(scrollbar_offset / (window_height - scrollbar_height) * max_scroll)
            elif event.type == pygame.VIDEORESIZE:
                # Limit window size within the specified range
                new_width, new_height = event.size
                new_width = max(MIN_WINDOW_SIZE[1], min(new_width, MAX_WINDOW_SIZE[1]))
                new_height = max(MIN_WINDOW_SIZE[0], min(new_height, MAX_WINDOW_SIZE[0]))
                window_width = new_width
                window_height = new_height
                window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                max_scroll = max((len(options) * ITEM_HEIGHT) - window_height, 0)

        # Adjust scroll offset to stay within range
        scroll_offset = max(min(scroll_offset, max_scroll), 0)

        pygame.display.flip()

        clock.tick(60)  # Limit to 60 FPS

    # Quit pygame
    pygame.quit()

def main():
    options = read_notepad(GIFT_LIST)
    if options:
        display_on_gui(options)

if __name__ == "__main__":
    main()
