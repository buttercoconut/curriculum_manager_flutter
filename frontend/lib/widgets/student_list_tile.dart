import 'package:flutter/material.dart';

class StudentListTile extends StatelessWidget {
  final String name;
  final String grade;

  const StudentListTile({Key? key, required this.name, required this.grade}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const Icon(Icons.person),
      title: Text(name),
      subtitle: Text('Grade: $grade'),
    );
  }
}
