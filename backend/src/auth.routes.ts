import { Router } from 'express';

import { AuthController } from './auth.controller';
import { authenticateToken } from './auth.middleware';
import { AuthenticateUserRequest, authenticateUserSchema } from './auth.types';
import { validateBody } from './validation.middleware';

const router = Router();
const authController = new AuthController();

router.post(
  '/signup',
  validateBody<AuthenticateUserRequest>(authenticateUserSchema),
  authController.signUp
);

router.post(
  '/signin',
  validateBody(authenticateUserSchema),
  authController.signIn
);

router.post('/signout', authenticateToken, authController.signOut);

export default router;
