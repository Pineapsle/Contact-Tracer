from flask import Blueprint, render_template, request, redirect
from app.logic.simulator import device_pool, simulate_proximity, refresh_tokens
from app.logic.diagnosis_server import upload_diagnosis_keys, get_diagnosis_keys
from app.logic.risk_evaluator import evaluate_all_devices

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    refresh_tokens()
    simulate_proximity()
    return render_template('index.html', devices=device_pool)

@bp.route('/device/<device_id>')
def view_device(device_id):
    device = next((d for d in device_pool if d.device_id == device_id), None)
    return render_template('device.html', device=device)

@bp.route('/diagnose/<device_id>', methods=['POST'])
def diagnose(device_id):
    device = next((d for d in device_pool if d.device_id == device_id), None)
    if device:
        upload_diagnosis_keys(device.upload_if_positive())
    return redirect('/')

@bp.route('/risk_check')
def risk_check():
    results = evaluate_all_devices(device_pool, get_diagnosis_keys())
    return render_template('risk_check.html', results=results)