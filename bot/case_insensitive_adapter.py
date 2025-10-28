from chatterbot.logic import BestMatch
from chatterbot.conversation import Statement


class CaseInsensitiveBestMatch(BestMatch):
    """
    A custom BestMatch logic adapter that compares text case-insensitively.
    """

    def compare_statements(self, statement, other_statement):
        """
        Override the comparison logic to make it case-insensitive.
        """
        # Lowercase both statements' text before comparing
        text1 = (statement.text or "").lower()
        text2 = (other_statement.text or "").lower()

        # Create lowercase Statement objects to pass into similarity function
        lower_stmt = Statement(text1)
        lower_other = Statement(text2)

        return super().compare_statements(lower_stmt, lower_other)


# Custom preprocessor to convert text to lowercase
def to_lowercase(statement):
    statement.text = statement.text.lower()
    return statement
