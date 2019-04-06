from django_elasticsearch_dsl import DocType, Index
from model.models import Course

courses = Index('courses')


@courses.doc_type
class CourseDocument(DocType):
	class Meta:

		model = Course

		fields = [
			'course_title',
			'course_description',
			'course_logo'
		]