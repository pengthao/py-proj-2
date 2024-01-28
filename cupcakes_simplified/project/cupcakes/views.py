from flask import Blueprint, render_template, redirect, url_for
from project.models import Cupcake
from project.cupcakes.forms import AddForm, DelForm

