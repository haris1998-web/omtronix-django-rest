# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone


class BulletinIssues(models.Model):
    year = models.IntegerField()
    number = models.IntegerField()
    published_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'bulletin_issues'
        unique_together = (('updated_at', 'id'), ('year', 'number'),)


class KonkurzRestrukturalizaciaActors(models.Model):
    corporate_body_name = models.CharField(max_length=1000, blank=True, null=True)
    cin = models.BigIntegerField(blank=True, null=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    building_number = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    postal_code = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'konkurz_restrukturalizacia_actors'


class KonkurzRestrukturalizaciaIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, models.CASCADE)
    raw_issue = models.OneToOneField('RawIssues', models.CASCADE)
    court_name = models.CharField(max_length=1000)
    file_reference = models.CharField(max_length=1000)
    ics = models.CharField(max_length=1000)
    released_by = models.CharField(max_length=1000)
    releaser_position = models.CharField(max_length=1000, blank=True, null=True)
    sent_by = models.CharField(max_length=1000, blank=True, null=True)
    released_date = models.DateField()
    debtor = models.ForeignKey(KonkurzRestrukturalizaciaActors, models.CASCADE, blank=True, null=True)
    kind = models.CharField(max_length=1000)
    heading = models.TextField(blank=True, null=True)
    decision = models.TextField(blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    advice = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'konkurz_restrukturalizacia_issues'
        unique_together = (('updated_at', 'id'),)


class KonkurzRestrukturalizaciaProposings(models.Model):
    issue = models.ForeignKey(KonkurzRestrukturalizaciaIssues, on_delete=models.CASCADE)
    actor = models.ForeignKey(KonkurzRestrukturalizaciaActors, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'konkurz_restrukturalizacia_proposings'


class KonkurzVyrovnanieIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, on_delete=models.CASCADE)
    raw_issue = models.OneToOneField('RawIssues', on_delete=models.CASCADE)
    court_code = models.CharField(max_length=1000)
    court_name = models.CharField(max_length=1000)
    file_reference = models.CharField(max_length=1000)
    corporate_body_name = models.CharField(max_length=1000)
    cin = models.BigIntegerField(blank=False, null=False)
    street = models.CharField(max_length=1000, blank=True, null=True)
    building_number = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    postal_code = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    kind_code = models.CharField(max_length=1000)
    kind_name = models.CharField(max_length=1000)
    announcement = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'konkurz_vyrovnanie_issues'
        unique_together = (('updated_at', 'id'),)


class LikvidatorIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, models.CASCADE)
    raw_issue = models.OneToOneField('RawIssues', models.CASCADE)
    legal_form_code = models.CharField(max_length=1000)
    legal_form_name = models.CharField(max_length=1000)
    corporate_body_name = models.CharField(max_length=1000)
    cin = models.BigIntegerField()
    sid = models.CharField(max_length=1000, blank=True, null=True)
    street = models.CharField(max_length=1000)
    building_number = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    postal_code = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    in_business_register = models.BooleanField()
    br_insertion = models.CharField(max_length=1000, blank=True, null=True)
    br_court_code = models.CharField(max_length=1000, blank=True, null=True)
    br_court_name = models.CharField(max_length=1000, blank=True, null=True)
    br_section = models.CharField(max_length=1000, blank=True, null=True)
    other_registrar_name = models.CharField(max_length=1000, blank=True, null=True)
    other_registration_number = models.CharField(max_length=1000, blank=True, null=True)
    decision_based_on = models.CharField(max_length=1000)
    decision_date = models.DateField()
    claim_term = models.CharField(max_length=1000)
    liquidation_start_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    debtee_legal_form_code = models.CharField(max_length=1000, blank=True, null=True)
    debtee_legal_form_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'likvidator_issues'
        unique_together = (('updated_at', 'id'),)


class OrPodanieIssueDocuments(models.Model):
    or_podanie_issue = models.ForeignKey('OrPodanieIssues', models.CASCADE)
    name = models.CharField(max_length=1000)
    delivery_date = models.DateField()
    ruz_deposit_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'or_podanie_issue_documents'


class OrPodanieIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, models.CASCADE)
    raw_issue = models.ForeignKey('RawIssues', models.CASCADE)
    br_mark = models.CharField(max_length=1000)
    br_court_code = models.CharField(max_length=1000)
    br_court_name = models.CharField(max_length=1000, blank=False, null=False)
    kind_code = models.CharField(max_length=1000)
    kind_name = models.CharField(max_length=1000)
    cin = models.BigIntegerField(blank=False, null=False)
    registration_date = models.DateField(blank=False, null=False)
    corporate_body_name = models.CharField(max_length=1000, blank=False, null=False)
    br_section = models.CharField(max_length=1000, blank=True, null=True)
    br_insertion = models.CharField(max_length=1000)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address_line = models.CharField(max_length=1000, blank=True, null=True)
    street = models.CharField(max_length=1000, blank=False, null=False)
    postal_code = models.CharField(max_length=1000, blank=False, null=False)
    city = models.CharField(max_length=1000, blank=False, null=False)

    class Meta:
        db_table = 'or_podanie_issues'
        ordering = ['-id']
        unique_together = (('updated_at', 'id'),)


class RawIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, models.CASCADE)
    file_name = models.CharField(max_length=1000)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'raw_issues'
        unique_together = (('updated_at', 'id'),)


class ZnizenieImaniaCeos(models.Model):
    znizenie_imania_issue = models.ForeignKey('ZnizenieImaniaIssues', models.CASCADE)
    prefixes = models.CharField(max_length=1000, blank=True, null=True)
    postfixes = models.CharField(max_length=1000, blank=True, null=True)
    given_name = models.CharField(max_length=1000, blank=True, null=True)
    family_name = models.CharField(max_length=1000, blank=True, null=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    building_number = models.CharField(max_length=1000, blank=True, null=True)
    postal_code = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'znizenie_imania_ceos'


class ZnizenieImaniaIssues(models.Model):
    bulletin_issue = models.ForeignKey(BulletinIssues, models.CASCADE)
    raw_issue = models.OneToOneField(RawIssues, models.CASCADE)
    corporate_body_name = models.CharField(max_length=1000)
    street = models.CharField(max_length=1000, blank=True, null=True)
    building_number = models.CharField(max_length=1000, blank=True, null=True)
    postal_code = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    br_court_code = models.CharField(max_length=1000)
    br_court_name = models.CharField(max_length=1000)
    br_section = models.CharField(max_length=1000)
    br_insertion = models.CharField(max_length=1000)
    cin = models.BigIntegerField()
    decision_text = models.TextField(blank=True, null=True)
    decision_date = models.DateField(blank=True, null=True)
    equity_currency_code = models.CharField(max_length=1000)
    old_equity_value = models.DecimalField(max_digits=12, decimal_places=2)
    new_equity_value = models.DecimalField(max_digits=12, decimal_places=2)
    resolution_store_date = models.DateField(blank=True, null=True)
    first_ov_released_date = models.DateField(blank=True, null=True)
    first_ov_released_number = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'znizenie_imania_issues'
        unique_together = (('updated_at', 'id'),)
