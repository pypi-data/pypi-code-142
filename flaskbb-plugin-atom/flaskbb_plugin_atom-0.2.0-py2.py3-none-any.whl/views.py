# -*- coding: utf-8 -*-
"""
    atom.views
    ~~~~~~~~~~

    This module contains the views for the
    atom Plugin.

    :copyright: (c) 2022 by exelotl.
    :license: MIT License, see LICENSE for more details.
"""
import math
from flask import Blueprint, flash, Response, current_app, url_for

from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry

from flaskbb.utils.settings import flaskbb_config

from flaskbb.forum.models import (Category, Forum, ForumsRead, Post, Topic, TopicsRead)

atom_bp = Blueprint("atom_bp", __name__, template_folder="templates")

def get_url_for_post(post: Post):
    
    post_in_topic = Post.query.filter(
        Post.topic_id == post.topic_id, Post.id <= post.id
    ).order_by(Post.id.asc()).count()
    
    page = int(math.ceil(post_in_topic / float(flaskbb_config["POSTS_PER_PAGE"])))
    
    url_kwargs = {
        "topic_id": post.topic.id,
        "page": page,
        "_anchor": f"pid{post.id}"
    }
    # if post.topic.slug:
    #     url_kwargs["slug"] = post.topic.slug
    return url_for("forum.view_topic", **url_kwargs)

@atom_bp.route("/")
def index():
    
    plugin = PluginRegistry.query.filter_by(name="atom").first()
    
    if plugin and not plugin.is_installed:
        return render_template("errors/page_not_found.html"), 404
    
    posts_query = Post.query.order_by(
        Post.id.desc()   # descending
    ).filter(
        # Unsure if this is rigorous enough. Do permissions make certain forums/categories hidden to guests?
        Post.hidden != True,
        Topic.id == Post.topic_id,
        Topic.hidden != True,
    ).limit(
        plugin.settings['limit']
    ).offset(0)
    
    posts = [(post, get_url_for_post(post)) for post in posts_query]
    
    project_title = flaskbb_config['PROJECT_TITLE']
    
    base_url = current_app.config['PREFERRED_URL_SCHEME'] + '://' + current_app.config['SERVER_NAME']
    
    # Technically this could be wrong, but close enough, I guess.
    feed_date_modified = posts[0][0].date_created
    
    output_html = plugin.settings['output_html']
    
    return Response(
        status = 200,
        response = render_template("feed.xml",
            plugin = plugin,
            posts = posts,
            base_url = base_url,
            project_title = project_title,
            feed_date_modified = feed_date_modified,
            output_html = output_html,
        ),
        mimetype = "application/atom+xml"
        # mimetype = "text/plain"
    )
