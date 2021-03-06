from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newCurriculum/', views.newCurriculum, name='newCurriculum'),
    path('departmentHead/', views.newHead, name='departmentHead'),
    path('newCourse/', views.newCourse, name='newCourse'),
    path('newTopic/', views.newTopic, name='newTopic'),
    path('newGoal/', views.newGoal, name='newGoal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editPerson/', views.editPerson, name='editPerson'),
    path('editCurriculum/', views.pickCuricToEdit, name='editCurriculum'),
    path('gradeDist/', views.gradeDist, name='gradeDist'),
    path('gradeGoal/<int:curr_pk>/<int:course_pk>/', views.gradeGoal, name='gradeGoal'),
    path('newSection/', views.newSection, name='newSection'),
    path('editCourse/', views.forkCourseManagement, name='editCourse'),
    path('editSpecificCurriculum/<int:curr_id>', views.editCurriculum, name='editSpecificCurriculum'),
    path('addCourseToCurric/<int:curr_pk>', views.addCourseToCurriculum, name='addCourseToCurriculum'),
    path('selectCourseForCurricEdit/<int:curr_pk>', views.pickCourseInCurriculumForEditing,
         name='selectCourseForCurricEdit'),
    path('editCCT/<int:curr_pk>/<int:course_pk>', views.editCCT, name='editCCT'),
    path('forkAddGradeCourseGoal/<int:curr_pk>/<int:course_pk>', views.forkGoal, name='forkAddGradeCourseGoal'),
    path('addGoalToCourse/<int:curr_pk>/<int:course_pk>', views.addGoalToCourse, name='addGoalToCourse'),
    path('editSpecificCourse/<int:course_pk>/', views.editCourse, name='addGoalToCourse'),
    path('addTopicToCourse/<int:course_pk>/', views.addTopicToCourse, name='addGoalToCourse'),
    path('addTopicToCurriculum/<int:curr_pk>/', views.addTopicToCurric, name='addTopicToCurr'),

    path('editSection/', views.editSection, name='editSection'),
    path('editTopic/', views.editTopic, name='editTopic'),
    path('editGoal/', views.editGoal, name='editGoal'),
    path('qPage/', views.qPage, name='qPage'),
    path('q1/', views.q1, name='q1'),
    path('q2/', views.q2, name='q2'),
    path('q3/', views.q3, name='q3'),
    path('q4/', views.q4, name='q4'),
    path('q5/', views.q5, name='q5'),

]
