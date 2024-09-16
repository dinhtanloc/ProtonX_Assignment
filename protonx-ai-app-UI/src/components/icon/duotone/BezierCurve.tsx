import React, { SVGProps } from 'react';

const SvgBezierCurve = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M4.953 14.303l-1.906-.606C4.65 8.644 7.673 6 12 6c4.327 0 7.349 2.644 8.953 7.697l-1.906.606C17.688 10.023 15.377 8 12 8s-5.688 2.022-7.047 6.303zM12 8a1 1 0 100-2 1 1 0 000 2z'
					fill='currentColor'
					opacity={0.3}
				/>
				<path
					d='M5.732 6h3.439a3.001 3.001 0 015.658 0h3.439a2 2 0 110 2h-3.439a3.001 3.001 0 01-5.658 0H5.732a2 2 0 110-2zM12 8a1 1 0 100-2 1 1 0 000 2zM4 19a3 3 0 110-6 3 3 0 010 6zm0-2a1 1 0 100-2 1 1 0 000 2zm16 2a3 3 0 110-6 3 3 0 010 6zm0-2a1 1 0 100-2 1 1 0 000 2z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgBezierCurve;
