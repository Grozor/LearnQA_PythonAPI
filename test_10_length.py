class TestMyProject:
    def test_input_text(self):
        phrase = input("Set a phrase (no more 15 symbols): ")
        allowed_length_of_phrase = 15
        current_length_of_phrase = len(phrase)

        assert current_length_of_phrase < allowed_length_of_phrase,\
            "Your phrase is longer than 15 symbols"
