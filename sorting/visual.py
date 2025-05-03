# import pygame
# import sys
# import time

# class Visualizer:
#     def __init__(self, width=800, height=600, bar_color=(100, 200, 255), bg_color=(30, 30, 30), fps=60):
#         pygame.init()
#         self.width = width
#         self.height = height
#         self.bar_color = bar_color
#         self.bg_color = bg_color
#         self.fps = fps
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         pygame.display.set_caption("Array Visualizer")
#         self.clock = pygame.time.Clock()
#         self.array = []
#         self.current_heights = []

#     def update_array(self, new_array, animation_duration=0.5):
#         """Animates transition from current to new array"""
#         if not self.array:
#             self.array = new_array[:]
#             self.current_heights = new_array[:]
#             self._draw()
#             self._handle_events()
#             return

#         start_time = time.time()
#         initial = self.current_heights[:]
#         target = new_array[:]
#         self.array = new_array[:]

#         while time.time() - start_time < animation_duration:
#             elapsed = time.time() - start_time
#             t = min(1, elapsed / animation_duration)
#             self.current_heights = [
#                 initial[i] + (target[i] - initial[i]) * t if i < len(target) else 0
#                 for i in range(len(target))
#             ]
#             self._draw()
#             self._handle_events()
#             self.clock.tick(self.fps)

#         self.current_heights = target[:]
#         self._draw()

   
#     def _draw(self):
#         self.screen.fill(self.bg_color)
#         if not self.current_heights:
#             pygame.display.flip()
#             return

#         max_val = max(self.current_heights)
#         bar_width = self.width / len(self.current_heights)

#         font = pygame.font.SysFont("Arial", 14)
#         for i, val in enumerate(self.current_heights):
#             x = i * bar_width
#             bar_height = (val / max_val) * (self.height * 0.9) if max_val != 0 else 0
#             y = self.height - bar_height

#             # Draw bar
#             pygame.draw.rect(
#                 self.screen,
#                 self.bar_color,
#                 pygame.Rect(x, y, bar_width - 2, bar_height)
#             )

#             # Draw number inside or above the bar
#             text_surface = font.render(str(int(val)), True, (255, 255, 255))
#             text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
#             self.screen.blit(text_surface, text_rect)

#         pygame.display.flip()


#     def _handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#     def finish_animation(self, final_color=(50, 255, 100), animation_duration=0.1):
#         """Animates a color transition to indicate sorting is complete."""
#         start_time = time.time()
#         steps = int(self.fps * animation_duration)

#         for step in range(steps):
#             t = step / steps  # interpolation factor
#             current_color = (
#                 int(self.bar_color[0] + (final_color[0] - self.bar_color[0]) * t),
#                 int(self.bar_color[1] + (final_color[1] - self.bar_color[1]) * t),
#                 int(self.bar_color[2] + (final_color[2] - self.bar_color[2]) * t),
#             )
#             self.screen.fill(self.bg_color)
#             max_val = max(self.current_heights) if self.current_heights else 1
#             bar_width = self.width / len(self.current_heights) if self.current_heights else 1

#             font = pygame.font.SysFont("Arial", 14)
#             for i, val in enumerate(self.current_heights):
#                 x = i * bar_width
#                 bar_height = (val / max_val) * (self.height * 0.9)
#                 y = self.height - bar_height

#                 pygame.draw.rect(
#                     self.screen,
#                     current_color,
#                     pygame.Rect(x, y, bar_width - 2, bar_height)
#                 )
#                 text_surface = font.render(str(int(val)), True, (255, 255, 255))
#                 text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
#                 self.screen.blit(text_surface, text_rect)

#             pygame.display.flip()
#             self._handle_events()
#             self.clock.tick(self.fps)

#         # Finally, lock in the final color
#         self.bar_color = final_color
#         self._draw()


#     def run_forever(self):
#         while True:
#             self._handle_events()
#             self._draw()
#             self.clock.tick(self.fps)

import pygame
import sys
import time

class Visualizer:
    def __init__(self, width=800, height=600, bar_color=(100, 200, 255), bg_color=(30, 30, 30), fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.bar_color = bar_color
        self.bg_color = bg_color
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Array Visualizer")
        self.clock = pygame.time.Clock()
        self.array = []
        self.current_heights = []

    def update_array(self, new_array, animation_duration=0.5):
        """Animates transition from current to new array with horizontal movement for swaps"""
        if not self.array:
            self.array = new_array[:]
            self.current_heights = new_array[:]
            self._draw()
            self._handle_events()
            return

        start_time = time.time()
        old_array = self.array[:]
        self.array = new_array[:]
        
        # Create a mapping of values to their new positions
        old_positions = {val: i for i, val in enumerate(old_array)}
        new_positions = {val: i for i, val in enumerate(new_array)}
        
        # Track both position and height for smooth animation
        position_data = []
        for i, val in enumerate(old_array):
            if i < len(new_array):
                start_pos = i
                end_pos = new_positions.get(val, i)  # Where this value ends up
                position_data.append({
                    'value': val,
                    'start_x': start_pos,
                    'end_x': end_pos,
                    'height': val
                })

        while time.time() - start_time < animation_duration:
            elapsed = time.time() - start_time
            t = min(1, elapsed / animation_duration)
            
            self.screen.fill(self.bg_color)
            max_val = max(new_array) if new_array else 1
            bar_width = self.width / len(new_array)
            font = pygame.font.SysFont("Arial", 14)
            
            # Draw bars at their interpolated positions
            for item in position_data:
                current_x = item['start_x'] + (item['end_x'] - item['start_x']) * t
                x = current_x * bar_width
                bar_height = (item['height'] / max_val) * (self.height * 0.9)
                y = self.height - bar_height

                # Draw bar
                pygame.draw.rect(
                    self.screen,
                    self.bar_color,
                    pygame.Rect(x, y, bar_width - 2, bar_height)
                )

                # Draw number
                text_surface = font.render(str(int(item['height'])), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
                self.screen.blit(text_surface, text_rect)
                
            pygame.display.flip()
            self._handle_events()
            self.clock.tick(self.fps)

        # Final state
        self.current_heights = new_array[:]
        self._draw()
   
    def _draw(self):
        self.screen.fill(self.bg_color)
        if not self.current_heights:
            pygame.display.flip()
            return

        max_val = max(self.current_heights)
        bar_width = self.width / len(self.current_heights)

        font = pygame.font.SysFont("Arial", 14)
        for i, val in enumerate(self.current_heights):
            x = i * bar_width
            bar_height = (val / max_val) * (self.height * 0.9) if max_val != 0 else 0
            y = self.height - bar_height

            # Draw bar
            pygame.draw.rect(
                self.screen,
                self.bar_color,
                pygame.Rect(x, y, bar_width - 2, bar_height)
            )

            # Draw number inside or above the bar
            text_surface = font.render(str(int(val)), True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def finish_animation(self, final_color=(50, 255, 100), animation_duration=0.1):
        """Animates a color transition to indicate sorting is complete."""
        start_time = time.time()
        steps = int(self.fps * animation_duration)

        for step in range(steps):
            t = step / steps  # interpolation factor
            current_color = (
                int(self.bar_color[0] + (final_color[0] - self.bar_color[0]) * t),
                int(self.bar_color[1] + (final_color[1] - self.bar_color[1]) * t),
                int(self.bar_color[2] + (final_color[2] - self.bar_color[2]) * t),
            )
            self.screen.fill(self.bg_color)
            max_val = max(self.current_heights) if self.current_heights else 1
            bar_width = self.width / len(self.current_heights) if self.current_heights else 1

            font = pygame.font.SysFont("Arial", 14)
            for i, val in enumerate(self.current_heights):
                x = i * bar_width
                bar_height = (val / max_val) * (self.height * 0.9)
                y = self.height - bar_height

                pygame.draw.rect(
                    self.screen,
                    current_color,
                    pygame.Rect(x, y, bar_width - 2, bar_height)
                )
                text_surface = font.render(str(int(val)), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()
            self._handle_events()
            self.clock.tick(self.fps)

        # Finally, lock in the final color
        self.bar_color = final_color
        self._draw()


    def run_forever(self):
        while True:
            self._handle_events()
            self._draw()
            self.clock.tick(self.fps)

