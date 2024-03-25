from django.db import models

# Create your models here.


#هدا الكلاس   Computer_engineering_1 يخص المرحلة الاولى
class Computer_engineering_1(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
        return f"{self.First_Name} {self.last_name} ({self.Division})"
    
class ComputerEngineering_1Request(models.Model):
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
   
    student = models.ForeignKey(Computer_engineering_1, on_delete=models.CASCADE,max_length=50,null=False)
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
   
    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"
class ComputerEngineering_11Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_1Request, on_delete=models.CASCADE, related_name='name_requests', null=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def __str__(self):
      return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"


#هدا الكلاس Computer_engineering_2 يخص المرحلة الثانية
class Computer_engineering_2(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
         return f"{self.First_Name} {self.last_name} ({self.Division})"
    
    
class  ComputerEngineering_2Request(models.Model):
    
    chair_CHOICES=[
      ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    student = models.ForeignKey(Computer_engineering_2, on_delete=models.CASCADE,max_length=50,null=False)

    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"
class ComputerEngineering_22Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_2Request, on_delete=models.CASCADE,max_length=50,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):

        self.status == 'Accepted'
            
        self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
        return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"
    

#هدا الكلاس Computer_engineering_3 يخص المرحلة الثالثة
class Computer_engineering_3(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
         return f"{self.First_Name} {self.last_name} ({self.Division})"
    
    
class  ComputerEngineering_3Request(models.Model):
    
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    
    student = models.ForeignKey(Computer_engineering_3, on_delete=models.CASCADE,max_length=50,null=False)
    
    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"

class ComputerEngineering_33Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_3Request, on_delete=models.CASCADE,max_length=50,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):

        self.status == 'Accepted'
            
        self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
       return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"
class Computer_engineering_32(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
         return f"{self.First_Name} {self.last_name} ({self.Division})"
    
    
class  ComputerEngineering_32Request(models.Model):
   
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    
    student = models.ForeignKey(Computer_engineering_32, on_delete=models.CASCADE,max_length=50,null=False)
    
    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"

class ComputerEngineering_332Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_32Request, on_delete=models.CASCADE,max_length=50,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):

        self.status == 'Accepted'
            
        self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
       return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"
    
#هدا الكلاس Computer_engineering_4 يخص المرحلة الرابعة
class Computer_engineering_4(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
        return f"{self.First_Name} {self.last_name} ({self.Division})"
    
    
class  ComputerEngineering_4Request(models.Model):
   
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    
    student = models.ForeignKey(Computer_engineering_4, on_delete=models.CASCADE,max_length=50,null=False)

    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"
class ComputerEngineering_44Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_4Request, on_delete=models.CASCADE,max_length=50,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):

        self.status == 'Accepted'
            
        self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
       return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"
class Computer_engineering_42(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
         return f"{self.First_Name} {self.last_name} ({self.Division})"
    
    
class  ComputerEngineering_42Request(models.Model):
   
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    
    student = models.ForeignKey(Computer_engineering_42, on_delete=models.CASCADE,max_length=50,null=False)
    
    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"

class ComputerEngineering_442Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    name = models.ForeignKey(ComputerEngineering_42Request, on_delete=models.CASCADE,max_length=50,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):

        self.status == 'Accepted'
            
        self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
        return f"({self.status}, Chair: {self.name.chair}, Student: {self.name})"
   
#هدا الكلاس يخص Cyber_security_1 المرحلة الاولى لقسم الامن السيبراني
class Cyber_security_1(models.Model):
    Division_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    First_Name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Division= models.CharField(max_length=10, choices=Division_CHOICES, blank=True)
    def __str__(self):
         return f"{self.First_Name} {self.last_name} ({self.Division})"
    
class  Cyber_security_1Request(models.Model):
    
    chair_CHOICES=[
       ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48')
    ]
    chair = models.CharField(max_length=10, choices=chair_CHOICES, default='Pending', blank=True, null=True)
    
    student = models.ForeignKey(Cyber_security_1, on_delete=models.CASCADE,max_length=50,null=False)
  

    def __str__(self):
        return f" {self.student.First_Name} {self.student.last_name}({self.student.Division})"
class Cyber_security_11Request(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    student = models.ForeignKey(Cyber_security_1Request, on_delete=models.CASCADE, max_length=50, null=False, related_name='requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)

    def accept_request(self):
     self.status = 'Accepted'
     self.save()

    def reject_request(self):
        self.status = 'Rejected'
        self.save() 
    
    def __str__(self):
       return f"({self.status}, Chair: {self.student.chair}, Student: {self.student})"
    


    
    
