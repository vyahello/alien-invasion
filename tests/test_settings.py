import pytest
from alien_invasion.settings import GameSettings, Settings


@pytest.fixture(scope="module")
def setup_settings():
    return GameSettings()


def test_screen_width(setup_settings):
    assert setup_settings.screen_width == 1200


def test_screen_height(setup_settings):
    assert setup_settings.screen_height == 600


def test_bg_color(setup_settings):
    assert setup_settings.bg_color == (31, 33, 39)


def test_ship_limit(setup_settings):
    assert setup_settings.ship_limit == 2


def test_fleet_drop_speed(setup_settings):
    assert setup_settings.fleet_drop_speed == 5


def test_fleet_direction(setup_settings):
    assert setup_settings.fleet_direction == 1


def test_bullet_width(setup_settings):
    assert setup_settings.bullet_width == 3


def test_bullet_height(setup_settings):
    assert setup_settings.bullet_height == 15


def test_bullet_color(setup_settings):
    assert setup_settings.bullet_color == (255, 255, 255)


def test_bullet_allowed(setup_settings):
    assert setup_settings.bullet_allowed == 15


def test_speedup_scale(setup_settings):
    assert setup_settings.speedup_scale == 1.1


def test_score_scale(setup_settings):
    assert setup_settings.score_scale == 1.5


def test_ship_speed_factor(setup_settings):
    assert setup_settings.ship_speed_factor == 5


def test_bullet_speed_factor(setup_settings):
    assert setup_settings.bullet_speed_factor == 3


def test_alien_speed_factor(setup_settings):
    assert setup_settings.alien_speed_factor == 2


def test_pause_count(setup_settings):
    assert setup_settings.pause_count == 2


def test_alien_points(setup_settings):
    assert setup_settings.alien_points == 50
