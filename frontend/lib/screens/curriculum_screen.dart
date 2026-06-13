import 'package:flutter/material.dart';
import '../widgets/curriculum_card.dart';

class CurriculumScreen extends StatelessWidget {
  const CurriculumScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Curriculum List')),
      body: ListView.builder(
        itemCount: 10,
        itemBuilder: (context, index) {
          return CurriculumCard(
            title: 'Curriculum $index',
            description: 'Description for curriculum $index',
          );
        },
      ),
    );
  }
}
