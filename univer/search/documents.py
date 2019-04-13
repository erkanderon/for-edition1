from django_elasticsearch_dsl import DocType, Index, fields
from model.models import Course, University

courses = Index('courses')


@courses.doc_type
class CourseDocument(DocType):
	belongs_to = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
	class Meta:

		model = Course

		fields = [
			'title',
			'description',
			'status',
			'price',
			'popularity',
			'count_subscriber',
			'level',
			'tag',
			'logo'
		]
#		related_models = [University]

	def get_queryset(self):
		"""Not mandatory but to improve performance we can select related in one sql request"""
		return super(CourseDocument, self).get_queryset().select_related(
		    'belongs_to'
		)