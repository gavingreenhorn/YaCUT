from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app
from .constants import DUPLICATE_SHORT_LINK, DEFAULT_OK
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form), 200
    input_long, input_short = form.original_link.data, form.custom_id.data
    if input_short and URLMap.get('short', input_short):
        flash(DUPLICATE_SHORT_LINK.format(
            short_link=input_short, end='!'))
        return render_template('index.html', form=form)
    url_map = URLMap.create(input_long, input_short)
    return (
        render_template(
            'index.html',
            form=form,
            link_message=DEFAULT_OK,
            shortcut=url_map.fully_qualified_short_link),
        HTTPStatus.OK)


@app.route('/<string:shortcut>')
def redirect_to_full_link(shortcut):
    link_pair = URLMap.get('short', shortcut)
    if link_pair:
        return redirect(link_pair.original)
    abort(404)
