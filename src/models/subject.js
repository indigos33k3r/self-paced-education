import mongoose from 'mongoose';
import Tag from './tag.js';

const Schema = mongoose.Schema;

export const Subject = new Schema({
    name: { type: String, required: true },
    tags: [ { type: Tag, required: true } ]
});
