import 'package:flutter/material.dart';
import '../widgets/grade_card.dart';

class GradeScreen extends StatelessWidget {
  const GradeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Grade Details')),
      body: ListView.builder(
        itemCount: 5,
        itemBuilder: (context, index) {
          return GradeCard(
            subject: 'Subject $index',
            score: (80 + index * 3).toDouble(),
          );
        },
      ),
    );
  }
}
