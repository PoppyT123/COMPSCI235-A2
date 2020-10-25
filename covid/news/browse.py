from flask import Blueprint, render_template
from flask import request, render_template, redirect, url_for, session
import covid.adapters.repository as repo
import covid.utilities.utilities as utilities
import covid.news.services as services
from covid.news import news
browse_blueprint = Blueprint(
    'browse_bp', __name__)


@browse_blueprint.route('/browse/search', methods=['GET', 'POST'])
def search():
    search_param = request.form.get('search_param')
    return news.articles_by_title(title=search_param)


@browse_blueprint.route('/browse', methods=['GET'])
def browse():
    return render_template('browse_by_title.html')