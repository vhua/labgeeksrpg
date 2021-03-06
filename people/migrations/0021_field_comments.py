# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        pass
        "Write your forwards methods here."

    def backwards(self, orm):
        for review in orm.UWLTReview.objects.all():
            review.comments += "\n\nteamwork_comments\n%s" % review.teamwork_comments
            review.comments += "\n\ncustomer_service_comments\n%s" % review.customer_service_comments
            review.comments += "\n\ndependability_comments\n%s" % review.dependability_comments
            review.comments += "\n\nintegrity_comments\n%s" % review.integrity_comments
            review.comments += "\n\ncommunication_comments\n%s" % review.communication_comments
            review.comments += "\n\ninitiative_comments\n%s" % review.initiative_comments
            review.comments += "\n\nattitude_comments\n%s" % review.attitude_comments
            review.comments += "\n\nproductivity_comments\n%s" % review.productivity_comments
            review.comments += "\n\ntechnical_knowledge_comments\n%s" % review.technical_knowledge_comments
            review.comments += "\n\nresponsibility_comments\n%s" % review.responsibility_comments
            review.comments += "\n\npolicies_comments\n%s" % review.policies_comments
            review.comments += "\n\nprocedures_comments\n%s" % review.procedures_comments
            review.comments += "\n\nmissed_shifts_comments\n%s" % review.missed_shifts_comments
            review.comments += "\n\ntardies_comments\n%s" % review.tardies_comments
            review.save()

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.employmentstatus': {
            'Meta': {'object_name': 'EmploymentStatus'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'people.paygrade': {
            'Meta': {'object_name': 'PayGrade'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'wage': ('django.db.models.fields.FloatField', [], {})
        },
        'people.performancereview': {
            'Meta': {'object_name': 'PerformanceReview'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_final': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_used_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reviewer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_review'", 'to': "orm['auth.User']"})
        },
        'people.title': {
            'Meta': {'object_name': 'Title'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pay_grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.PayGrade']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'workgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.WorkGroup']"})
        },
        'people.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'alt_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'badge_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'call_me_by': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'grad_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'site_skin': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'staff_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.EmploymentStatus']", 'null': 'True', 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'supervisor'", 'null': 'True', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Title']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uwnetid'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'wage': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.WageHistory']", 'null': 'True', 'blank': 'True'}),
            'working_periods': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['schedule.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'people.uwltreview': {
            'Meta': {'object_name': 'UWLTReview', '_ormbases': ['people.PerformanceReview']},
            'attitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'attitude_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'communication': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'communication_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'customer_service': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'customer_service_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dependability': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dependability_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'initiative_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'integrity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'integrity_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'missed_shifts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'missed_shifts_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'performancereview_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.PerformanceReview']", 'unique': 'True', 'primary_key': 'True'}),
            'policies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'policies_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'procedures': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'procedures_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'productivity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'productivity_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'responsibility': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'responsibility_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tardies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tardies_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'teamwork': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teamwork_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'technical_knowledge': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'technical_knowledge_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'people.wagechangereason': {
            'Meta': {'object_name': 'WageChangeReason'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'people.wagehistory': {
            'Meta': {'object_name': 'WageHistory'},
            'effective_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'wage': ('django.db.models.fields.FloatField', [], {}),
            'wage_change_reason': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.WageChangeReason']"})
        },
        'people.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'schedule.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 5, 14)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 5, 14)'})
        }
    }

    complete_apps = ['people']
