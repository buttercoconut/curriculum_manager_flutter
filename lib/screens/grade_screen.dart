import 'package:flutter/material.dart';
import '../models/grade.dart';
import '../services/api_service.dart';

class GradeScreen extends StatefulWidget {
  const GradeScreen({Key? key}) : super(key: key);

  @override
  State<GradeScreen> createState() => _GradeScreenState();
}

class _GradeScreenState extends State<GradeScreen> {
  late Future<List<Grade>> _grades;

  @override
  void initState() {
    super.initState();
    _grades = ApiService.fetchGrades();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Grade List'),
      ),
      body: FutureBuilder<List<Grade>>(
        future: _grades,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final grades = snapshot.data ?? [];
          return ListView.builder(
            itemCount: grades.length,
            itemBuilder: (context, index) {
              final grade = grades[index];
              return ListTile(
                title: Text(grade.name),
                subtitle: Text('Class: ${grade.className}'),
                trailing: Text('Students: ${grade.studentCount}'),
              );
            },
          );
        },
      ),
    );
  }
}
