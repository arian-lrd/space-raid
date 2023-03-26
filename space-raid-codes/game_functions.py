import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import json
from explosion import Explosion
from alien_bullet import AlienBullet

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats,
                         aliens, sb, ai_sounds, explosions, alien_bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, ai_sounds, aliens, alien_bullets)
    elif event.key == pygame.K_q:
        with open('all_time_high.json') as f_obj:
            number = f_obj.readline()
            if stats.high_score >= int(number):
                store_all_time_high(stats)
        sys.exit()  # TODO: Add something before this to store the all_time high score
    elif event.key == pygame.K_p and not stats.game_active:
        # Reset the game settings
        ai_sounds.stop_menu_music()
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets)


def start_game(ai_settings, screen, stats, sb,  ship, aliens, bullets, ai_sounds, explosions, alien_bullets):
    """Start the game whenever called, 1) through key_down_events
    2) through check_play_button"""
    # Reset the game settings
    ai_settings.initialize_dynamic_settings()
    # Hide the mouse cursor
    pygame.mouse.set_visible(False)
    # Reset game statics.
    stats.reset_stats()
    stats.game_active = True

    # Load the all_time_high_score
    load_all_time_high(stats)

    # Reset the scoreboard images.
    sb.prep_score()
    sb.prep_level()
    sb.prep_high_score()
    sb.prep_ships()

    # Empty th list of bullets and aliens.
    bullets.empty()
    aliens.empty()
    explosions.empty()
    alien_bullets.empty()

    # Create a new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    ai_sounds.play_background_music()


def stop_background_music():
    """Stop the background music at the end of the game."""
    pygame.mixer.music.stop()


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y, ai_sounds, explosions, alien_bullets):
    """Start a new game when the player hits the button."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        ai_sounds.stop_menu_music()
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets)


def check_keyup_events(ship, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets, ai_sounds, explosions, alien_bullets):
    """Respond to key presses and mouse movements."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('all_time_high.json') as f_obj:
                number = f_obj.readline()
                if stats.high_score >= int(number):
                    store_all_time_high(stats)
            sys.exit()  # TODO: Add something before this to store the all_time high score

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets,
                                 stats, aliens, sb, ai_sounds, explosions, alien_bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y, ai_sounds, explosions, alien_bullets)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets, play_button):
    """Update position of the bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()
    alien_bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= ai_settings.screen_height:
            alien_bullets.remove(alien_bullet)


    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets, ai_sounds, explosions, alien_bullets)
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        explosion = Explosion(ship.rect.centerx, ship.rect.centery, 3)
        explosions.add(explosion)
        if stats.ships_left != 0:
            ai_sounds.play_ship_explosion_sound()

        update_screen(ai_settings, screen, stats, sb,  ship, aliens, bullets,
                  play_button, explosions, alien_bullets)
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets)


def update_explosions(explosions):
    """Update the explosions and show them."""
    # Update explosion positions
    explosions.update()



def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets, ai_sounds, explosions, alien_bullets):
    """Respond to bullet_alien collisions."""
    # Remove the bullets that have collided.
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    with open('all_time_high.json') as f_obj:
        number = f_obj.readline()
        if stats.high_score >= int(number):
            store_all_time_high(stats)

    for alien in collisions:
        explosion = Explosion(alien.rect.centerx, alien.rect.centery, 2)
        explosions.add(explosion)



    if collisions:
        for alienss in collisions.values():
            stats.score += ai_settings.alien_points * len(alienss)
            ai_sounds.play_alien_explosion_sound()
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)


def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """If the entire fleet is destroyed, start a new level."""
    # Destroy the existing bullets, speed up the game, and create new fleet
    bullets.empty()
    alien_bullets.empty()
    ai_settings.increase_speed()

    # Increase level.
    stats.level += 1
    sb.prep_level()
    create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets, ai_sounds, aliens, alien_bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        # Create a new bullet and add it to the bullets group
        ai_sounds.play_laser_sound()
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    if len(alien_bullets) < ai_settings.alien_bullets_allowed:
        new_alien_bullet = AlienBullet(ai_settings, screen, aliens, ship)
        alien_bullets.add(new_alien_bullet)


def create_fleet(ai_settings, screen, ship,  aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,
                                  ship.rect.height, alien.rect.height)

    # Create a fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_number * 2 * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * row_number * alien.rect.height
    aliens.add(alien)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets):
    stats.first_try = False
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        revive_player(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions, alien_bullets) # TODO: inja sleep darim
    else:
        ai_sounds.play_gameover_sound()
        re_set_to_menu(stats, ai_sounds)


def re_set_to_menu(stats, ai_sounds):
    """If the player loses re-set the menu."""
    stop_background_music()
    ai_sounds.play_menu_music()
    stats.game_active = False
    pygame.mouse.set_visible(True)


def draw_game_over(screen):
    """Draw a game over message on screen if the player loses."""
    screen_rect = screen.get_rect()
    gameover_color = (255, 255, 255)
    gameover_bg_color = (171, 2, 2)
    font_gameover = pygame.font.Font('fonts/space_invaders copy.ttf', 100)
    gameover_image = font_gameover.render('Game Over', True, gameover_color, gameover_bg_color)

    gameover_image_rect = gameover_image.get_rect()
    gameover_image_rect.centerx = screen_rect.centerx
    gameover_image_rect.centery = screen_rect.centery - 200

    screen.blit(gameover_image, gameover_image_rect)


def draw_instructions(screen):
    """Draw the game instructions onto the screen."""
    screen_rect = screen.get_rect()
    instructions_color = (255, 255, 255)
    instructions_bg_color = (171, 2, 2)
    font_instructions1 = pygame.font.Font('fonts/Arial Bold Italic.ttf', 20)
    instructions_image1 = font_instructions1.render("  To start the game: click on the play button or press 'P'  ", True, instructions_color)

    instructions_image1_rect = instructions_image1.get_rect()
    instructions_image1_rect.centerx = screen_rect.centerx
    instructions_image1_rect.centery = screen_rect.bottom - (instructions_image1_rect.height * 2 + 10)

    screen.blit(instructions_image1, instructions_image1_rect)


    font_instructions2 = pygame.font.Font(
        'fonts/Arial Bold Italic.ttf', 20)
    instructions_image2 = font_instructions2.render(
        "  To quit the game: click on the close button or press 'Q'  ", True,
        instructions_color)

    instructions_image2_rect = instructions_image2.get_rect()
    instructions_image2_rect.centerx = screen_rect.centerx
    instructions_image2_rect.top = instructions_image1_rect.bottom + 5

    screen.blit(instructions_image2, instructions_image2_rect)


def draw_game_title(screen):
    """Draw the game's title in the beginning menu."""
    screen_rect = screen.get_rect()
    title_color = (255, 255, 255)
    title_bg_color = (171, 2, 2)
    font_title = pygame.font.Font('fonts/INVASION2000 copy.ttf', 100)
    title_image = font_title.render('Alien Invasion', True, title_color)

    title_image_rect = title_image.get_rect()
    title_image_rect.centerx = screen_rect.centerx
    title_image_rect.centery = screen_rect.top + 150

    screen.blit(title_image, title_image_rect)



def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, play_button, alien_bullets):
    """Check if the fleet is at an edge,
    and then update the position of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    # Look for alien_ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        explosion = Explosion(ship.rect.centerx, ship.rect.centery, 3)
        explosions.add(explosion) # TODO: inja add ship explosion darim
        if stats.ships_left != 0:
            ai_sounds.play_ship_explosion_sound()
        update_screen(ai_settings, screen, stats, sb,  ship, aliens, bullets,
                  play_button, explosions, alien_bullets)
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets) # TODO: inja sleep darim
    # Look for aliens hitting the bottom of the sscreen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets)
    aliens.update()


def update_screen(ai_settings, screen, stats, sb,  ship, aliens, bullets,
                  play_button, explosions, alien_bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.blit(ai_settings.bg_image_done, (0, 0))
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_alien_bullet()


    ship.blitme()
    aliens.draw(screen)
    explosions.draw(screen)

    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()
        draw_instructions(screen)
        if not stats.first_try:
            sleep(0.5)
            draw_game_over(screen)
        else:
            draw_game_title(screen)

    # Make most recently drawn screen visible.
    pygame.display.flip()


def revive_player(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions, alien_bullets):
    """If the player has any lives left revive them."""
    # Decrement ships_left.
    stats.ships_left -= 1

    # Update scoreboard(ship images)
    sb.prep_ships()

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    alien_bullets.empty()
    explosions.empty()

    # Create a new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


    # Pause.
    sleep(0.5) # TODO: inja sleep darim


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets):
    """Check if any aliens have reached the bottom of the screen.
    If so Initialize another round"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            if stats.ships_left != 0:
                ai_sounds.play_alien_reach_bottom_sound()
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ai_sounds, explosions, alien_bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have hit an edge."""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop th entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_high_score(stats, sb):
    """Check to see if there is a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def store_all_time_high(stats):
    """Store the all time high score."""
    filepath = '/PATH_ON_YOUR_SYSTEM'
    with open(filepath, 'w') as f_obj:
        json.dump(stats.high_score, f_obj)


def load_all_time_high(stats):
    """Load all time high score """
    filepath = '/PATH_ON_YOUR_SYSTEM'
    with open(filepath, 'r') as f_obj:
        all_time_high = json.load(f_obj)
        stats.high_score = all_time_high

