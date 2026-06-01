import 'package:flutter/material.dart';
import '../models/student.dart';

class StudentListTile extends StatelessWidget {
  final Student student;

  const StudentListTile({Key? key, required this.student}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Icon(Icons.person)),
      title: Text(student.name),
      subtitle: Text('Grade: ${student.gradeLevel} | Class: ${student.className}'),
      trailing: const Icon(Icons.arrow_forward),
      onTap: () {
        // Navigate to student detail if needed
      },
    );
  }
}
