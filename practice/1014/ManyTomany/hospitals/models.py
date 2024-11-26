from django.db import models

'''
# M
# Doctor 모델에서 Patient에 접근하려면 역참조
# patient_set
class Doctor(models.Model):
  name = models.TextField()
  def __str__(self):
    return f'{self.pk}번 의사 {self.name}'
  
# N
# Patient 모델에서 Doctor접근하려면 참조
# doctors 속성
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor)
  name = models.TextField()

  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
    '''
'''
# ORM 코드
doctor1 = Doctor.objects.create(name = 'alice')
patient1 = Patient.objects.create(name = 'carol')
patient2 = Patient.objects.create(name = 'duke')
# 1번 patient1에 doctor1추가
patient1.doctors.add(doctor1)
# 2번 doctor1에 patient2추가
doctor1.patient_set.add(patient2)
# 3번 doctor1에 patient1제거
doctor1.patient_set.remove(patient1)
'''

class Doctor(models.Model):
  name = models.TextField()
  def __str__(self):
    return f'{self.pk}번 의사 {self.name}'

# Doctor와 Patient사이의 관계를 Reservation 모델을 통해 관리 하겠다!!
# through = 'Reservations'
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor, through='Reservation')
  name = models.TextField()

  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
  
class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  symptom = models.TextField()
  reserver_at = models.DateTimeField(auto_now_add=True)
'''
doctor1 = Doctor.objects.create(name = 'alice')
patient1 = Patient.objects.create(name = 'carol')
patient2 = Patient.objects.create(name = 'duke')

# 1. reservation class를 통한 예약
# alice가 carol을 두통(headache)로 예약
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()

# 2. Patient 객체 통한 예약
# duke가 alice로 감기(flue)로 예약
patient2.doctors.add(doctor1, through_defaults={'symptom' : 'flu'})


# 3. alice 목요일에 지방 출장을 가게되서
# carol과 한 예약 취소
doctor1.patient_set.remove(patient1)
'''