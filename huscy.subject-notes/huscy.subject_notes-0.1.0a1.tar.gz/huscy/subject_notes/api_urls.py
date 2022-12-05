from rest_framework.routers import DefaultRouter

from huscy.subject_notes.views import SubjectNoteViewSet, SubjectNoteTagViewSet
from huscy.subjects.urls import subject_router

router = DefaultRouter()
router.register('subjectnotetags', SubjectNoteTagViewSet, basename='subjectnotetag')

subject_router.register('notes', SubjectNoteViewSet, basename='subjectnote')


urlpatterns = router.urls
urlpatterns += subject_router.urls
