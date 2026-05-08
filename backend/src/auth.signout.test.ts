import express from 'express';
import request from 'supertest';
import { describe, expect, it } from 'vitest';

import { AuthController } from './auth.controller';

const buildApp = () => {
  const app = express();
  const controller = new AuthController();
  app.post('/auth/signout', controller.signOut);
  return app;
};

describe('POST /auth/signout', () => {
  it('returns a success message', async () => {
    const app = buildApp();

    const response = await request(app).post('/auth/signout');

    expect(response.status).toBe(200);
    expect(response.body).toEqual({ message: 'Signed out successfully' });
  });
});
