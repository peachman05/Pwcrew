from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings

DATE_INPUT_FORMATS = ('%d/%m/%Y')


province_list =(

        ('กรุงเทพมหานคร', 'กรุงเทพมหานคร'),
        ('กระบี่', 'กระบี่'),
        ('กาญจนบุรี', 'กาญจนบุรี'),
        ('กาฬสินธุ์', 'กาฬสินธุ์' ),
        ('กำแพงเพชร', 'กำแพงเพชร' ),
        ('ขอนแก่น', 'ขอนแก่น' ),
        ('จันทบุรี', 'จันทบุรี' ),
        ('ฉะเชิงเทรา', 'ฉะเชิงเทรา' ),
        ('ชลบุรี', 'ชลบุรี' ),
        ('ชัยนาท', 'ชัยนาท' ),
        ('ชัยภูมิ', 'ชัยภูมิ' ),
        ('ชุมพร', 'ชุมพร' ),
        ('เชียงราย', 'เชียงราย' ),
        ('เชียงใหม่', 'เชียงใหม่' ),
        ('ตรัง', 'ตรัง' ),
        ('ตราด', 'ตราด' ),
        ('ตาก', 'ตาก' ),
        ('นครนายก', 'นครนายก' ),
        ('นครปฐม', 'นครปฐม' ),
        ('นครพนม', 'นครพนม' ),
        ('นครราชสีมา', 'นครราชสีมา' ),
        ('นครศรีธรรมราช', 'นครศรีธรรมราช' ),
        ('นครสวรรค์', 'นครสวรรค์' ),
        ('นนทบุรี', 'นนทบุรี' ),
        ('นราธิวาส', 'นราธิวาส' ),
        ('น่าน', 'น่าน' ),
        ('บึงกาฬ', 'บึงกาฬ' ),
        ('บุรีรัมย์', 'บุรีรัมย์' ),
        ('ปทุมธานี', 'ปทุมธานี' ),
        ('ประจวบคีรีขันธ์', 'ประจวบคีรีขันธ์' ),
        ('ปราจีนบุรี', 'ปราจีนบุรี' ),
        ('ปัตตานี', 'ปัตตานี' ),
        ('พระนครศรีอยุธยา', 'พระนครศรีอยุธยา' ),
        ('พังงา', 'พังงา' ),
        ('พัทลุง', 'พัทลุง' ),
        ('พิจิตร', 'พิจิตร' ),
        ('พิษณุโลก', 'พิษณุโลก' ),
        ('เพชรบุรี', 'เพชรบุรี' ),
        ('เพชรบูรณ์', 'เพชรบูรณ์' ),
        ('แพร่', 'แพร่' ),
        ('พะเยา', 'พะเยา' ),
        ('ภูเก็ต', 'ภูเก็ต' ),
        ('มหาสารคาม', 'มหาสารคาม' ),
        ('มุกดาหาร', 'มุกดาหาร' ),
        ('แม่ฮ่องสอน', 'แม่ฮ่องสอน' ),
        ('ยะลา', 'ยะลา' ),
        ('ยโสธร', 'ยโสธร' ),
        ('ร้อยเอ็ด', 'ร้อยเอ็ด' ),
        ('ระนอง', 'ระนอง' ),
        ('ระยอง', 'ระยอง' ),
        ('ราชบุรี', 'ราชบุรี' ),
        ('ลพบุรี', 'ลพบุรี' ),
        ('ลำปาง', 'ลำปาง' ),
        ('ลำพูน', 'ลำพูน' ),
        ('เลย', 'เลย' ),
        ('ศรีสะเกษ', 'ศรีสะเกษ' ),
        ('สกลนคร', 'สกลนคร' ),
        ('สงขลา', 'สงขลา' ),
        ('สตูล', 'สตูล' ),
        ('สมุทรปราการ', 'สมุทรปราการ' ),
        ('สมุทรสงคราม', 'สมุทรสงคราม' ),
        ('สมุทรสาคร', 'สมุทรสาคร' ),
        ('สระแก้ว', 'สระแก้ว' ),
        ('สระบุรี', 'สระบุรี' ),
        ('สิงห์บุรี', 'สิงห์บุรี' ),
        ('สุโขทัย', 'สุโขทัย' ),
        ('สุพรรณบุรี', 'สุพรรณบุรี' ),
        ('สุราษฎร์ธานี', 'สุราษฎร์ธานี' ),
        ('สุรินทร์', 'สุรินทร์' ),
        ('หนองคาย', 'หนองคาย' ),
        ('หนองบัวลำภู', 'หนองบัวลำภู' ),
        ('อ่างทอง', 'อ่างทอง' ),
        ('อุดรธานี', 'อุดรธานี' ),
        ('อุทัยธานี', 'อุทัยธานี' ),
        ('อุตรดิตถ์', 'อุตรดิตถ์' ),
        ('อุบลราชธานี', 'อุบลราชธานี' ),
        ('อำนาจเจริญ', 'อำนาจเจริญ' ),
      
    )


TITLE_LIST = (
        ('Mr.(นาย)', 'Mr.(นาย)'),
        ('Mrs.(นาง)', 'Mrs.(นาง)'),
        ('Miss.(นางสาว)', 'Miss.(นางสาว)'),
    )


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>''
    extention = filename.split('.')[1]
    path = 'picture/user_{0}/profile.{1}'.format(instance.user.username,extention)
    return  path

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    
    # image = models.FileField(upload_to='documents/', blank=True)
    image = models.FileField(upload_to=user_directory_path, blank=True)
    title = models.CharField("คำนำหน้าชื่อ",max_length=15,choices=TITLE_LIST, blank=True)
    firstname_thai = models.CharField("ชื่อจริง(ไทย)", max_length=30, blank=True)
    lastname_thai = models.CharField("นามสกุล(ไทย)", max_length=30, blank=True)
    firstname_eng = models.CharField("ชื่อจริง(English)",max_length=30, blank=True)
    lastname_eng = models.CharField("นามสกุล(English)",max_length=30, blank=True)
    card_number = models.CharField("เลขบัตรประชาชน",max_length=20, blank=True)
    religion_LIST = (
        ('พุทธ', 'พุทธ'),
        ('คริสต์', 'คริสต์'),
        ('อิสลาม', 'อิสลาม'),
        ('อื่นๆ', 'อื่นๆ'),
    )
    religion = models.CharField("ศาสนา",max_length=20, choices=religion_LIST, blank=True)
    BLOOD_TYPE_LIST = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    blood_type = models.CharField("กรุ๊ปเลือด",max_length=6,choices=BLOOD_TYPE_LIST, blank=True)
    birth_date = models.DateField('วัน/เดือน/ปี เกิด',blank=True,null=True)
    email =  models.EmailField("Email",max_length=60, blank=True)
    STATUS_LIST = (
        ('แต่งงาน', 'แต่งงาน'),
        ('โสด', 'โสด'),
        ('หย่า', 'หย่า'),
        ('หม้าย', 'หม้าย'),
    )
    status = models.CharField("สถานะ",max_length=10,choices=STATUS_LIST, blank=True)
    domicile_province = models.CharField("ภูมิลำเนาเดิม จังหวัด",max_length=30, choices=province_list, blank=True)

    spouse_title = models.CharField("คำนำหน้าชื่อ", max_length=15,choices=TITLE_LIST, blank=True)
    firstname_spouse_thai = models.CharField("ชื่อจริง(ไทย)", max_length=30, blank=True)
    lastname_spouse_thai = models.CharField("นามสกุล(ไทย)", max_length=30, blank=True)
    firstname_spouse_eng = models.CharField("ชื่อจริง(English)", max_length=30, blank=True)
    lastname_spouse_eng = models.CharField("นามสกุล(English)", max_length=30, blank=True)

    FATHER_TITLE_LIST = (
        ('Mr.(นาย)', 'Mr.(นาย)'),
    )
    father_title = models.CharField("คำนำหน้าชื่อ", max_length=15,default='MR',choices=FATHER_TITLE_LIST, blank=True)
    firstname_father_thai = models.CharField("ชื่อจริง(ไทย)", max_length=30, blank=True)
    lastname_father_thai = models.CharField("นามสกุล(ไทย)", max_length=30, blank=True)
    firstnamename_father_eng = models.CharField("ชื่อจริง(English)", max_length=30, blank=True)
    lastname_father_eng = models.CharField("นามสกุล(English)", max_length=30, blank=True)

    MOTHER_TITLE_LIST = (
        ('Mrs.(นาง)', 'Mrs.(นาง)'),
        ('Miss.(นางสาว)', 'Miss.(นางสาว)'),
    )
    mother_title = models.CharField("คำนำหน้าชื่อ", max_length=15,choices=MOTHER_TITLE_LIST, blank=True)
    firstname_mother_thai = models.CharField("ชื่อจริง(ไทย)", max_length=30, blank=True)
    lastname_mother_thai = models.CharField("นามสกุล(ไทย)", max_length=30, blank=True)
    firstname_mother_eng = models.CharField("ชื่อจริง(English)", max_length=30, blank=True)
    lastname_mother_eng = models.CharField("นามสกุล(English)",max_length=30, blank=True)

    def __str__(self):
        return self.user.username

class PersonalInfoForm(ModelForm):
    class Meta:
        model = PersonalInfo
        exclude = ['user','card_number']

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        # self.fields['firstname_thai'].widget.attrs['size'] = 20
        self.fields['birth_date'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    number_regis = models.CharField("เลขที่",max_length=10, blank=True)
    village_no_regis = models.CharField("หมู่",max_length=10, blank=True)
    village_name_regis = models.CharField("หมู่บ้าน",max_length=40, blank=True)
    lane_regis = models.CharField("ซอย",max_length=40, blank=True) # ซอย
    road_regis = models.CharField("ถนน",max_length=70, blank=True)
    sub_district_regis = models.CharField("ตำบล",max_length=70, blank=True)
    district_regis = models.CharField("อำเภอ",max_length=70, blank=True)
    province_regis = models.CharField("จังหวัด",max_length=70, blank=True, choices=province_list)
    postal_code_regis = models.CharField("รหัสไปรษณีย์",max_length=10, blank=True)
    smartphone_number_regis = models.CharField("เบอร์มือถือ",max_length=20, blank=True)
    phone_number_regis = models.CharField("เบอร์โทรบ้าน",max_length=20, blank=True)

    number = models.CharField("เลขที่",max_length=10, blank=True)
    village_no = models.CharField("หมู่",max_length=10, blank=True)
    village_name = models.CharField("หมู่บ้าน",max_length=40, blank=True)
    lane = models.CharField("ซอย",max_length=40, blank=True) # ซอย
    road = models.CharField("ถนน",max_length=70, blank=True)
    sub_district = models.CharField("ตำบล",max_length=70, blank=True)
    district = models.CharField("อำเภอ",max_length=70, blank=True)
    province = models.CharField("จังหวัด",max_length=70, blank=True, choices=province_list)
    postal_code = models.CharField("รหัสไปรษณีย์",max_length=10, blank=True)
    smartphone_number = models.CharField("เบอร์มือถือ",max_length=20, blank=True)
    phone_number = models.CharField("เบอร์โทรบ้าน",max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class AddressForm(ModelForm):
    class Meta:
        model = Address
        # fields = ['number_regis', 'village_no_regis', 'village_name_regis']
        # fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['number_regis'].widget.attrs['size'] = 5


class WorkInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    start_service_date = models.DateField(verbose_name='วันเข้ารับราชการ',blank=True,null=True)
    position = models.CharField('ตำแหน่ง', max_length=30, blank=True)
    affiliation = models.CharField('สังกัด', max_length=30, blank=True) #สังกัด
    end_service_date = models.DateField('วันเกษียณอายุราชการ', blank=True,null=True)
    POSITION_LIST = (
        ('ครูผู้ช่วย', 'ครูผู้ช่วย'),
        ('ครู', 'ครู'),
        ('รองผู้อำนวยการ', 'รองผู้อำนวยการ'),
        ('ผู้อำนวยการ', 'ผู้อำนวยการ'),
    )
    current_position = models.CharField('ตำแหน่งปัจจุบัน', max_length=60, blank=True, choices=POSITION_LIST)
    position_number = models.CharField('เลขที่ตำแหน่ง', max_length=20, blank=True)
    RANK_LIST = (
        ('ค.ศ.1', 'ค.ศ.1'),
        ('ค.ศ.2', 'ค.ศ.2'),
        ('ค.ศ.3(2)', 'ค.ศ.3(2)'),
        ('ค.ศ.3', 'ค.ศ.3'),
        ('ค.ศ.4(3)', 'ค.ศ.4(3)'),
        ('ค.ศ.4', 'ค.ศ.4'),
    )
    rank_number = models.CharField('อันดับ', max_length=20, blank=True, choices=RANK_LIST)
    rank_money = models.IntegerField('ขั้น', default=0, blank=True)
    academic_standing = models.CharField('วิทยฐานะ', max_length=20, blank=True)
    academic_standing_money = models.IntegerField('เงินวิทยฐานะ', default=0, blank=True)

    start_PW_date = models.DateField('วันที่ดำรงตำแหน่งที่โรงเรียนปทุมวิไล',blank=True,null=True)

    GPF_LIST = (
        ('เป็น', 'เป็น'),
        ('ไม่เป็น', 'ไม่เป็น'),
    )
    isGPF_member = models.CharField('สมาชิก กบข.', max_length=20, blank=True, choices=GPF_LIST)
    DEPARTMENT_LIST = (
        ('ฝ่ายบริหาร', 'ฝ่ายบริหาร'),
        ('กลุ่มสาระการเรียนรู้วิทยาศาสตร์', 'กลุ่มสาระการเรียนรู้วิทยาศาสตร์'),
        ('กลุ่มสาระการเรียนรู้คณิตศาสตร์', 'กลุ่มสาระการเรียนรู้คณิตศาสตร์'),
        ('กลุ่มสาระการเรียนรู้ศิลปะ', 'กลุ่มสาระการเรียนรู้ศิลปะ'),        
        ('กลุ่มสาระการเรียนรู้ภาษาไทย', 'กลุ่มสาระการเรียนรู้ภาษาไทย'),
        ('กลุ่มสาระการเรียนรู้ภาษาต่างประเทศ', 'กลุ่มสาระการเรียนรู้ภาษาต่างประเทศ'),
        ('กลุ่มสาระการเรียนรู้สังคมศึกษา ศาสนา และวัฒนธรรม', 'กลุ่มสาระการเรียนรู้สังคมศึกษา ศาสนา และวัฒนธรรม'),
        ('กลุ่มสาระการเรียนรู้การงานอาชีพและเทคโนโลยี', 'กลุ่มสาระการเรียนรู้การงานอาชีพและเทคโนโลยี'),
        ('กลุ่มสาระการเรียนรู้สุขศึกษาและพลศึกษา', 'กลุ่มสาระการเรียนรู้สุขศึกษาและพลศึกษา'),  
    )
    department = models.CharField('กลุ่มสาระ', max_length=60, blank=True, choices=DEPARTMENT_LIST)
    subject = models.CharField('วิชาที่สอน', max_length=60, blank=True, null=True)

    def __str__(self):
        return self.user.username


class WorkInfoForm(ModelForm):
    class Meta:
        model = WorkInfo
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(WorkInfoForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['start_service_date'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['end_service_date'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['start_PW_date'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['end_service_date'].widget.attrs['disabled'] = "disabled"
        self.fields['academic_standing'].widget.attrs['readonly'] = True


class Insignia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    class1 = models.CharField('ชั้น',max_length=60, blank=True)
    date1 = models.DateField('วัน/เดือน/ปี ที่ได้รับ',blank=True,null=True)

    def __str__(self):
        return self.user.username

class InsigniaForm(ModelForm):
    class Meta:
        model = Insignia
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(InsigniaForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['date1'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')

       
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    acronym_bachelor = models.CharField('อักษรย่อ', max_length=10, blank=True)
    major_field_bachelor = models.CharField('สาขาวิชาเอก', max_length=40, blank=True)
    minor_field_bachelor = models.CharField('สาขาวิชาโท', max_length=40, blank=True)
    university_bachelor = models.CharField('สถาบัน', max_length=70,default='', blank=True)
    start_year_bachelor = models.DateField('ปีที่เริ่มศึกษา', blank=True,null=True)
    end_year_bachelor = models.DateField('ปีที่สำเร็จการศึกษา', blank=True,null=True)

    acronym_master = models.CharField('อักษรย่อ', max_length=10, blank=True)
    major_field_master = models.CharField('สาขาวิชาเอก', max_length=40, blank=True)
    minor_field_master = models.CharField('สาขาวิชาโท',max_length=40, blank=True)
    university_master = models.CharField('สถาบัน', max_length=70,default='', blank=True)
    start_year_master = models.DateField('ปีที่เริ่มศึกษา', blank=True,null=True)
    end_year_master = models.DateField('ปีที่สำเร็จการศึกษา', blank=True,null=True)

    acronym_phd = models.CharField('อักษรย่อ', max_length=10, blank=True)
    major_field_phd = models.CharField('สาขาวิชาเอก', max_length=40, blank=True)
    minor_field_phd = models.CharField('สาขาวิชาโท', max_length=40, blank=True)
    university_phd = models.CharField('สถาบัน', max_length=70,default='', blank=True)
    start_year_phd = models.DateField('ปีที่เริ่มศึกษา', blank=True,null=True)
    end_year_phd = models.DateField('ปีที่สำเร็จการศึกษา', blank=True,null=True)

    def __str__(self):
        return self.user.username


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['start_year_bachelor'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['end_year_bachelor'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')

        self.fields['start_year_master'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['end_year_master'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')

        self.fields['start_year_phd'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')
        self.fields['end_year_phd'].input_formats = ('%d-%m-%Y','%Y-%m-%d','%d/%m/%Y','%d//%m//%Y')


class NewsInHome2(models.Model):
    news = models.TextField('ข้อความ',max_length=1000, blank=True)

class NewsInHome2Form(ModelForm):
    class Meta:
        model = NewsInHome2
        fields = ['news']