import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_add_new_book_invalid_name(self, collector):
        collector.add_new_book("")  # Пустое название
        collector.add_new_book("A" * 41)  # Слишком длинное название
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Несуществующий жанр")  # Неправильный жанр
        collector.set_book_genre("Несуществующая книга", "Фантастика")  # Неправильная книга
        assert collector.get_book_genre("Гарри Поттер") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга 1"]

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_for_children() == ["Книга 1"]

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")  # Повторное добавление
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    def test_delete_non_existent_book_from_favorites(self, collector):
        collector.delete_book_from_favorites("Несуществующая книга")  # Не должно вызывать ошибок
        assert True  # Просто проверяем, что не упало