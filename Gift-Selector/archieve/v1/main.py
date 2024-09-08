# imports
import pygame
import random

# Constants
GIFT_LIST = 'gifts.txt'
ITEM_HEIGHT = 30  # Height of each item in the menu
SCROLL_SPEED = 20  # Speed of scrolling
MIN_WINDOW_SIZE = (300, 400)
MAX_WINDOW_SIZE = (1050, 1000)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCROLLBAR_COLOR = (150, 150, 150)
SCROLLBAR_BUTTON_COLOR = (100, 100, 100)
BUTTON_COLOR_SAVE = (255, 255, 0)
BUTTON_COLOR_SAVE_HOVER = (255, 255, 150)
BUTTON_COLOR_REFRESH = (0, 255, 0)
BUTTON_COLOR_REFRESH_HOVER = (150, 255, 150)
BUTTON_COLOR_EXIT = (255, 0, 0)
BUTTON_COLOR_EXIT_HOVER = (255, 150, 150)
MESSAGE_COLOR = (255, 255, 0)

def unique_list(options):
    """Return a unique set of options."""
    return list(set(options))

def shuffle_contents(options):
    """Shuffle the options list."""
    random.shuffle(options)

def list_to_string(selected_list):
    """Convert a list to a single string."""
    if selected_list is None:
        print("No valid list found.")
        return ""
    try:
        return ' '.join(str(item) for item in selected_list)
    except ValueError:
        print("Invalid input! Please enter a valid list.")
        return ""

def read_notepad(notepad):
    """Read the contents of a notepad file and return a shuffled unique list of lines."""
    try:
        with open(notepad, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Number of lines read from the file: {len(lines)}")
            shuffle_contents(lines)
            unique_lines = unique_list(lines)
            print(f"Number of lines after shuffling: {len(unique_lines)}")
            return unique_lines
    except FileNotFoundError:
        print("File not found!")
        return []

def save_top_10(options):
    """Save the top 10 options to a file."""
    top_10 = [option.strip().title() for option in options[:10]]
    with open('top_10.txt', 'w') as file:
        file.write('\n'.join(top_10))
    return "Top 10 have been saved."

def convert_to_title_case(option):
    """Convert each word in the option to title case, preserving '(s)' suffix."""
    words = option.strip().split()
    for i, word in enumerate(words):
        if word.lower().endswith("(s)"):
            base_word = word[:-3]
            words[i] = f"{base_word.title()}(s)"
        elif not word.isupper():
            words[i] = word.title()
    return ' '.join(words)

def draw_button(window, font, text, rect, base_color, hover_color, is_hover):
    """Draw a button on the window."""
    color = hover_color if is_hover else base_color
    pygame.draw.rect(window, color, rect)
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, rect)

def display_on_gui(options):
    """Display the options on a Pygame GUI with scrolling and buttons."""
    pygame.init()
    
    window_height = 550
    window_width = 550
    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Gift Options Ranked at Random")

    font = pygame.font.SysFont("Arial", 24)
    bold_font = pygame.font.SysFont("Arial", 24, bold=True)
    message_font = pygame.font.SysFont("Arial", 20)

    text_color = WHITE
    background_color = BLACK

    scroll_offset = 0
    is_scrolling = False
    scroll_start_pos = 0

    message_text = ""
    message_alpha = 255
    message_display_time = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        window.fill(background_color)

        title_surface = bold_font.render(f"{len(options)} Gift Options Ranked at Random", True, text_color)
        title_height = title_surface.get_height()
        window.blit(title_surface, ((window_width - title_surface.get_width()) // 2, 10 - scroll_offset))

        save_top_10_text = "Save Top 10"
        refresh_button_text = "Refresh"
        exit_button_text = "Exit"
        
        save_top_10_rect = pygame.Rect(window_width - 150, window_height - 120, 130, 40)
        refresh_button_rect = pygame.Rect(window_width - 150, window_height - 80, 130, 40)
        exit_button_rect = pygame.Rect(window_width - 150, window_height - 40, 130, 40)
        
        draw_button(window, bold_font, save_top_10_text, save_top_10_rect, BUTTON_COLOR_SAVE, BUTTON_COLOR_SAVE_HOVER, save_top_10_rect.collidepoint(pygame.mouse.get_pos()))
        draw_button(window, bold_font, refresh_button_text, refresh_button_rect, BUTTON_COLOR_REFRESH, BUTTON_COLOR_REFRESH_HOVER, refresh_button_rect.collidepoint(pygame.mouse.get_pos()))
        draw_button(window, bold_font, exit_button_text, exit_button_rect, BUTTON_COLOR_EXIT, BUTTON_COLOR_EXIT_HOVER, exit_button_rect.collidepoint(pygame.mouse.get_pos()))

        if message_text:
            message_surface = message_font.render(message_text, True, (*MESSAGE_COLOR, message_alpha))
            window.blit(message_surface, (window_width - 325, 50)) # (10, window_height - 50)
            if pygame.time.get_ticks() - message_display_time > 3000:
                message_alpha -= 3
                if message_alpha <= 0:
                    message_text = ""
                    message_alpha = 255
            else:
                message_display_time = pygame.time.get_ticks()

        height_adjustment = title_height + 20
        total_height = len(options) * ITEM_HEIGHT
        max_scroll = max(total_height - window_height, 0)
        y = height_adjustment - scroll_offset

        if max_scroll > 0:
            scrollbar_height = (window_height * window_height) / total_height
            scrollbar_offset = (scroll_offset * (window_height - scrollbar_height)) / max_scroll
            pygame.draw.rect(window, SCROLLBAR_COLOR, (window_width - 20, 0, 20, window_height))
            pygame.draw.rect(window, SCROLLBAR_BUTTON_COLOR, (window_width - 20, scrollbar_offset, 20, scrollbar_height))

        for idx, option in enumerate(options, start=1):
            option_text = convert_to_title_case(option)
            numbered_text = f"{idx}. {option_text}"
            text_surface = font.render(numbered_text, True, text_color)
            if y < window_height - ITEM_HEIGHT and y + ITEM_HEIGHT > 0:
                window.blit(text_surface, (10, y))
            y += ITEM_HEIGHT

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
                        message_display_time = pygame.time.get_ticks()
                    elif refresh_button_rect.collidepoint(event.pos):
                        shuffle_contents(options)
                        message_text = "Contents of the list have been refreshed."
                        message_display_time = pygame.time.get_ticks()
                    elif exit_button_rect.collidepoint(event.pos):
                        running = False
                    elif window_width - 20 <= event.pos[0] <= window_width:
                        if max_scroll > 0:
                            scrollbar_height = window_height * window_height / total_height
                            scrollbar_offset = scroll_offset * (window_height - scrollbar_height) / max_scroll
                            if scrollbar_offset <= event.pos[1] <= scrollbar_offset + scrollbar_height:
                                is_scrolling = True
                                scroll_start_pos = event.pos[1] - scrollbar_offset
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_scrolling = False
            elif event.type == pygame.MOUSEMOTION:
                if is_scrolling:
                    new_scrollbar_offset = event.pos[1] - scroll_start_pos
                    if max_scroll > 0:
                        scrollbar_height = window_height * window_height / total_height
                        scrollbar_offset = min(max(new_scrollbar_offset, 0), window_height - scrollbar_height)
                        scroll_offset = int(scrollbar_offset / (window_height - scrollbar_height) * max_scroll)
            elif event.type == pygame.VIDEORESIZE:
                new_width, new_height = event.size
                window_width = max(MIN_WINDOW_SIZE[0], min(new_width, MAX_WINDOW_SIZE[0]))
                window_height = max(MIN_WINDOW_SIZE[1], min(new_height, MAX_WINDOW_SIZE[1]))
                window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                max_scroll = max(total_height - window_height, 0)

        scroll_offset = max(0, min(scroll_offset, max_scroll))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def main():
    options = read_notepad(GIFT_LIST)
    if options:
        display_on_gui(options)

if __name__ == "__main__":
    main()
