import 'package:flutter/material.dart';
import 'screens/curriculum_screen.dart';
import 'screens/student_screen.dart';
import 'screens/grade_screen.dart';

void main() {
  runApp(const CurriculumManagerApp());
}

class CurriculumManagerApp extends StatelessWidget {
  const CurriculumManagerApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Curriculum Manager',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const CurriculumScreen(),
      routes: {
        '/curriculum': (_) => const CurriculumScreen(),
        '/student': (_) => const StudentScreen(),
        '/grade': (_) => const GradeScreen(),
      },
    );
  }
}
