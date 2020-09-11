from controllers.BaseController import *


class PostController:
    @staticmethod
    def get_post_data(post_id):
        p = Post.select().where(Post.id == post_id).first() or None
        if isinstance(p, Post):
            post_data = {
                'author_id': User.select().where(User.login == p.author).first().id,
                'author': p.author,
                'auto': is_auth(),
                'login': session['login'] if session.get('login', False) else '',
                'text': p.text,
                'post_title': p.title
            }
            return post_data
        else:
            raise ArithmeticError

    @staticmethod
    def create_post():
        if is_auth():
            title = request.form['title'].strip().title()
            text = request.form['text'].strip()  # убираем пробелы с боков

            validation_result = PostController.validation_post_data(title, text)
            if isinstance(validation_result, bool):
                p = Post(title=title, text=text, author=session['login'], slug=slugify(title))
                p.save()
            else:
                return redirect(url_for('my_work', message=validation_result))
        return redirect(url_for('index'))

    @staticmethod
    def updata_post(post_id, new_text):
        pass

    @staticmethod
    def delete_post(post_id):
        if is_auth():
            p = Post.select().where(Post.id == post_id).first()
            if p.author == session['login']:
                p.delete_instance()
                redirect(url_for('index'))
            redirect(url_for('error_404'))
        redirect(url_for('error_404'))

    @staticmethod
    def validation_post_data(title, text):
        # control max-min lenght/ min-title 6 char, max 60
        # min-text 100 char, max 4k
        # find and delete uncorectable sign, start whit digital-char
        # find doublicate char following each other more 4

        text_len = len(text)
        title_len = len(title)
        digital_char = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        if (text_len > 4000 or
                text_len < 100 or
                title_len > 60 or
                title_len < 6):
            return 'lenght error\nmin-title 6 char, max 60\nmin-text 100 char, max 4k'

        if text[0] in digital_char or title[0] in digital_char:
            return 'start whit digital-char is uncorectable'

        triggers = find_trigger_char(title + ' ' + text)
        if triggers:
            return 'your text have mush more characters following each other(4max)<br> on char num: ' + str(triggers)

        return True
