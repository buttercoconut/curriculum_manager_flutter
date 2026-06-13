import 'package:flutter/material.dart';
import '../widgets/student_list_tile.dart';

class StudentScreen extends StatelessWidget {
  const StudentScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Student List')),
      body: ListView.builder(
        itemCount: 10,
        itemBuilder: (context, index) {
          return StudentListTile(
            name: 'Student $index',
            grade: 'Grade ${index % 3 + 1}',
          );
        },
      ),
    );
  }
}
