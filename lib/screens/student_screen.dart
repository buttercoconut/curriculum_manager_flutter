import 'package:flutter/material.dart';
import '../widgets/student_list_tile.dart';
import '../models/student.dart';
import '../services/api_service.dart';

class StudentScreen extends StatefulWidget {
  const StudentScreen({Key? key}) : super(key: key);

  @override
  State<StudentScreen> createState() => _StudentScreenState();
}

class _StudentScreenState extends State<StudentScreen> {
  late Future<List<Student>> _students;

  @override
  void initState() {
    super.initState();
    _students = ApiService.fetchStudents();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student List'),
      ),
      body: FutureBuilder<List<Student>>(
        future: _students,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final students = snapshot.data ?? [];
          return ListView.builder(
            itemCount: students.length,
            itemBuilder: (context, index) {
              return StudentListTile(student: students[index]);
            },
          );
        },
      ),
    );
  }
}
