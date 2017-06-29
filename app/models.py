"""
Define application models.
"""
from datetime import datetime


# local imports
from app import db


class User(db.Model):
    """
    Define user fields.
    Contains attributes for a user
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


class Challenge(db.Model):
    """
    Define challenge fields.
    Contains attributes for a programming challenge.
    """

    __tablename__ = 'challenges'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(5000), index=True, nullable=False)
    developer_level = db.Column(db.Integer, nullable=False)


class Language(db.Model):
    """
    Define programming language fields.
    """

    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, nullable=False)


class LanguageUser(db.Model):
    """
    Define programming language user fields.
    """

    __tablename__ = 'language_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))


class Review(db.Model):
    """
    Define review fields.
    Contain attributes defining code review.
    """

    __tablename__ = 'reviewers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.String(1500), index=True, nullable=False)


class UserChallenge(db.Model):
    """
    Define user-challenge fields.
    Contains attributes for attempted programming challenges.
    """

    __tablename__ = 'user_challenges'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_solution = db.Column(db.String(5000), index=True, nullable=False)
    challenge_status = db.Column(db.String(30), nullable=False, default="not started")
    started_at = db.Column(db.DateTime, default=datetime.now)
    completed_at = db.Column(db.DateTime, default=None)


