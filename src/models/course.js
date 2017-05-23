import mongoose from 'mongoose';
import Subject from './subject.js';
import Tag from './tag.js';

const Schema = mongoose.Schema;

export const Course = new Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    instructor: { type: String, required: true },
    source: { type: String, required: true },
    url: { type: String, required: true },
    subjects: [ { type: Subject, required: true } ],
    tags: [ { type: Tag, required: true } ]
});
