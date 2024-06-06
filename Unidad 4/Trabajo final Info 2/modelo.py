import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.io import loadmat

class SistemaGestionModelo:
    def __init__(self):
        self.doctores = {"Fulano":"123"}
        self.pacientes = {}
    def validarDoctor(self,usuario,contrasena):
        if usuario in self.doctores.keys():
            if self.doctores[usuario]==contrasena:
                return True
            else:
                return False
        else:
            return False
    def agregar_doctor(self, usuario, contraseña):
        if usuario in self.doctores.keys():
            return True
        else:
            self.doctores[usuario] = contraseña
        print("Doctor agregado exitosamente.")
        print(self.doctores)
    def agregar_paciente(self, nombre, apellido, edad, identificacion, fecha):
        if identificacion in self.pacientes.keys():
            return True
        else:
            self.pacientes[identificacion] = {"nombre": nombre, 
                                                "apellido": apellido, 
                                                "edad": edad,
                                                "identificacion": identificacion,
                                                "fecha": fecha}
        print(self.pacientes)
    def diagnosticar_paciente(self, fs=1000, f_p=1, f_qrs=0.5, pr_interval_start=0.2, pr_interval_end=0.7):
        ecg_signal= self.cargar_ekg(fs, f_p, f_qrs, pr_interval_start, pr_interval_end)
        pr_duration = float(pr_interval_end) - float(pr_interval_start)
        if pr_duration < 0.20:
            diagnostico = "Posible bloqueo cardíaco: intervalo PR corto."
            return diagnostico
        elif self.detectar_bloqueo_tipo_I(ecg_signal, fs)==True:
            diagnostico = "Bloqueo AV de primer grado"
            return diagnostico
        elif self.detectar_bloqueo_mobitz_I(ecg_signal, fs)==True:
            diagnostico = "Bloqueo AV de segundo grado tipo Mobitz I."
            return diagnostico
        elif self.detectar_bloqueo_mobitz_II(ecg_signal)==True:
            diagnostico = "Bloqueo AV de segundo grado tipo Mobitz II."
            return diagnostico
        elif self.detectar_bloqueo_tipo_III(ecg_signal)==True:
            diagnostico = "Bloqueo AV de tercer grado (completo)."
            return diagnostico
        else:
            diagnostico = "Intervalo PR normal."
            return diagnostico
    def detectar_bloqueo_tipo_I(self, ecg_signal, fs, pr_threshold=0.20):
    # Duración del intervalo PR en segundos para considerarlo como bloqueo tipo I
        pr_threshold_samples = float(float(pr_threshold) * float(fs))
        pr_duration = sum(1 for sample in ecg_signal if sample==0)
        if pr_duration > pr_threshold_samples:
                    return True
        return False
    def detectar_bloqueo_mobitz_I(self, ecg_signal, fs):
        # Duración máxima del intervalo PR para considerarlo como bloqueo Mobitz I
        max_pr_duration = 0.20 * int(fs)  # Convertir de segundos a muestras
        # Buscar el alargamiento progresivo del intervalo PR y la desaparición del complejo QRS
        pr_intervals = []
        qrs_detected = False
        for i, sample in enumerate(ecg_signal):
            if sample == 0 and not qrs_detected:
                continue  # Evitar falsas detecciones
            elif sample != 0 and not qrs_detected:
                qrs_detected = True
            elif sample == 0 and qrs_detected:
                pr_intervals.append(i)
                qrs_detected = False
        # Calcular la duración de los intervalos PR y verificar si hay bloqueo Mobitz I
        for i in range(len(pr_intervals) - 1):
            pr_duration = pr_intervals[i + 1] - pr_intervals[i]
            if pr_duration > max_pr_duration:
                return True
        return False
    def detectar_bloqueo_mobitz_II(self, ecg_signal):
        p_wave_count = 0  # Contador de ondas P
        qrs_detected = False  # Indicador de detección de complejo QRS
        pr_intervals = []  # Lista para almacenar los intervalos PR
        # Buscar las características del bloqueo Mobitz II
        for sample in ecg_signal:
            if sample == 0 and not qrs_detected:
                continue  # Evitar falsas detecciones
            elif sample != 0 and not qrs_detected:
                qrs_detected = True
            elif sample == 0 and qrs_detected:
                p_wave_count += 1
            elif sample != 0 and qrs_detected:
                if p_wave_count >2:
                    return True
                p_wave_count=0
                qrs_detected=False
        return False
    def detectar_bloqueo_tipo_III(self, ecg_signal):
        p_wave_detected = False  # Indicador de detección de onda P
        qrs_detected = False  # Indicador de detección de complejo QRS
        # Buscar la disociación entre las ondas P y los complejos QRS
        for sample in ecg_signal:
            if sample == 0 and not qrs_detected:
                continue  # Evitar falsas detecciones
            elif sample != 0 and not qrs_detected:
                qrs_detected = True
            elif sample == 0 and qrs_detected:
                p_wave_detected = True
            elif sample != 0 and qrs_detected and p_wave_detected:
                return True
            elif sample != 0 and qrs_detected and not p_wave_detected:
            # Si se detecta un complejo QRS sin una onda P asociada, reiniciar los indicadores
                qrs_detected = False
                p_wave_detected = False
        return False
    def cargar_ekg(self, fs=1000, f_p=1, f_qrs=0.5, pr_interval_start=0.1, pr_interval_end=0.2):
        t = np.linspace(0, 1, int(fs))  
        ecg_signal = (
                np.sin(2 * np.pi * int(f_p) * t) +  
                np.sin(2 * np.pi * float(f_qrs) * t)  
        ) * 0.5  
        return ecg_signal
    