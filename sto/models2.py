from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(db_column='CustNameID', primary_key = True)  # CJS added primary key =true for DJANGO.
    name = models.CharField(db_column='CustName', primary_key=True, max_length=100)  # Field name made lowercase.
    url = models.CharField(db_column='CustWebAddr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CustCategory', max_length=20, blank=True, null=True)  # Field name made lowercase.
    custdesignfeatures = models.TextField(db_column='CustDesignFeatures', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='CustEnteredBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entered_date = models.DateTimeField(db_column='CustEnteredDate', blank=True, null=True)  # Field name made lowercase.
    msa = models.CharField(db_column='CustMSA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msa_details = models.TextField(db_column='CustMSA_Details', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblS_Customers'
        
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    contact_id = models.AutoField(db_column='CC_ConID', primary_key=True)  # Field name made lowercase.
    complocid = models.IntegerField(db_column='CC_CompLocID')  # Field name made lowercase.
    city = models.CharField(db_column='CC_CustCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_first = models.CharField(db_column='CC_Name_First', max_length=50)  # Field name made lowercase.
    name_middle = models.CharField(db_column='CC_Name_Middle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_last = models.CharField(db_column='CC_Name_Last', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='CC_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonedirect = models.CharField(db_column='CC_PhoneDirect', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cell = models.CharField(db_column='CC_Cell', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pager = models.CharField(db_column='CC_Pager', max_length=50, blank=True, null=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='CC_Home_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='CC_Desc', max_length=50)  # Field name made lowercase.
    ext = models.CharField(db_column='CC_Ext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='CC_Birthday', blank=True, null=True)  # Field name made lowercase.
    spouse = models.CharField(db_column='CC_Spouse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='CC_Notes', blank=True, null=True)  # Field name made lowercase.
    rec_newsletter = models.BooleanField(db_column='CC_Rec_Newsletter')
    no_newsletter = models.NullBooleanField(db_column='CC_No_Newsletter')
    full_name = models.CharField(db_column='CC_Full_Name', max_length=50)  # Field name made lowercase.
    title_courtesy = models.CharField(db_column='CC_Title_Courtesy', max_length=8)  # Field name made lowercase.
    title_suffix = models.CharField(db_column='CC_Title_Suffix', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cc_type = models.CharField(db_column='CC_Type', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='CC_Status', max_length=10)  # Field name made lowercase.
    dtlastchg = models.DateTimeField(db_column='CC_DtLastChg', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='CC_EnteredBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entereddate = models.DateTimeField(db_column='CC_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='CC_ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='CC_ModifiedDate', blank=True, null=True)  # Field name made lowercase.
      # Field name made lowercase.
    prospect = models.NullBooleanField(db_column='CC_Prospect')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblS_CustContact'
        
    def __str__(self):
        return self.name