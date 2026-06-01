import 'package:flutter/material.dart';
import 'package:curriculum_manager_flutter/screens/curriculum_screen.dart';
import 'package:curriculum_manager_flutter/screens/student_screen.dart';
import 'package:curriculum_manager_flutter/screens/grade_screen.dart';

void main() {
  runApp(const CurriculumManagerApp());
}

class CurriculumManagerApp extends StatelessWidget {
  const CurriculumManagerApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Curriculum Manager',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const CurriculumScreen(),
        '/students': (context) => const StudentScreen(),
        '/grades': (context) => const GradeScreen(),
      },
    );
  }
}
