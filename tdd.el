;; -*- lexical-binding: t -*-

;; Eval this buffer to turn on TDD-esque test automation in
;; emacs. Basically, whever you save a file under in the project, this
;; will run the tests.  You'll probably need to modify the "rootdir"
;; value to make this work for your machine.
;;
;; Note that tests currently run very slowly because they each have to
;; spawn a process. Hmmm...

(require 'deferred)

(defun version-probe-tests ()
  (lexical-let ((rootdir "/Users/sixtynorth/projects/python_version_probe")
        ;;(dir (file-name-directory load-file-name))
        (filename (buffer-file-name (current-buffer)))
        (output-buffer "*version-probe-tests*"))
    (when (and (string-prefix-p rootdir filename)
	       (equal major-mode 'python-mode)
	       (get-buffer-create output-buffer))
      
      (with-current-buffer output-buffer
        (read-only-mode 0)
        (erase-buffer))
      
      (deferred:$

        (deferred:$
          (deferred:process-shell
            (format "cd %s && python3 -m unittest discover version_probe/test" rootdir)))

        ;; error
        (deferred:error it
          (lambda (err) (error-message-string err)))

        ;; finally
        (deferred:nextc it
          (lambda (x) x))
        
        (deferred:nextc it
          (lambda (output)
            (with-current-buffer output-buffer
              (insert output)
              (compilation-mode 1))
            (display-buffer output-buffer)))))))

(add-hook 'after-save-hook 'version-probe-tests)
