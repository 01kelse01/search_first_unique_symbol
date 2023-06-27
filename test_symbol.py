from my_script import search_first_unique_symbol


#
# def test_answer():
#     text = """The Tao gave birth to machine language.  Machine language gave birth
#             to the assembler.
#             The assembler gave birth to the compiler.  Now there are ten thousand
#             languages.
#             Each language has its purpose, however humble.  Each language
#             expresses the Yin and Yang of software.  Each language has its place within
#             the Tao.
#             But do not program in COBOL if you can avoid it.
#                     -- Geoffrey James, "The Tao of Programming"""
#     assert search_first_unique_symbol(text) == 'm'


class TestClass:
    def test_one(self):
        text = """The Tao gave birth to machine language.  Machine language gave birth
                    to the assembler.
                    The assembler gave birth to the compiler.  Now there are ten thousand
                    languages.
                    Each language has its purpose, however humble.  Each language
                    expresses the Yin and Yang of software.  Each language has its place within
                    the Tao.
                    But do not program in COBOL if you can avoid it.
                            -- Geoffrey James, "The Tao of Programming"""
        assert search_first_unique_symbol(text) == 'm'

    def test_two(self):
        text = """C makes it easy for you to shoot yourself in the foot. 
        C++ makes that harder, but when you do, it blows away your whole leg. 
        (с) Bjarne Stroustrup"""
        assert search_first_unique_symbol(text) == 'e'
